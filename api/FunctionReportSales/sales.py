"""sales.py

Sales push bot for the hourly report of sales figures
The script preloads the txt files with each query. 
It uses the functions of the src.utils_bot module to modify the result of the queries. 
With the information, it generates the report and sends it to Telegram using the src.bot module.


The script needs the installation of the following packages:
* os: For path management and directory creation
* pandas: Return a DataFrame object
* dotenv: Load environment variables
* logging: Log management

This script uses the following custom modules:
* src: Adapt the format of the data to be printed on Telegram

"""
import os
import pandas as pd
from .src import db
# import src.db as db
from .src import bot
# import src.bot as bot
from .src import utils_bot
# import src.utils_bot as utils_bot
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()
# Define project main path
MAIN_FOLDER = os.getenv('MAIN_PATH')

# LOG File save
logging.basicConfig(
    format= '%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
    )

################################## Query Load #####################################

query_path = os.path.join(MAIN_FOLDER, 'queries')

SL_company_conversion_day = open(os.path.join(query_path,
                    'SL_company_conversion_day.sql'), 'r').read()

SL_total_conversion_day = open(os.path.join(query_path,
                    'SL_total_conversion_day.sql'), 'r').read()

SL_company_conversion_hour = open(os.path.join(query_path,
                    'SL_company_conversion_hour.sql'), 'r').read()

SL_total_conversion_hour = open(os.path.join(query_path,
                    'SL_total_conversion_hour.sql'), 'r').read()

SL_staff_day = open(os.path.join(query_path,
                    'SL_staff_day.sql'), 'r').read()


SL_staff_hour= open(os.path.join(query_path,
                    'SL_staff_hour.sql'), 'r').read()


def main(GROUP_ID):
    """Main function, it is in charge of:
    * Query the database
    * Transform dataframes to strings
    * Assemble report
    * Send report to Telegram
    """    
    date =  pd.Timestamp.now().strftime('%A, %d %B %H:%M')
    # Today's conversion Report queries to the database
    today1 = utils_bot.df_more_two_cols(db.sql_to_df(SL_company_conversion_day))
    today2 = utils_bot.trans_one_row(db.sql_to_df(SL_total_conversion_day))

    # Hour conversion Report queries to the database
    hour1 = utils_bot.df_more_two_cols(db.sql_to_df(SL_company_conversion_hour))
    hour2 = utils_bot.trans_one_row(db.sql_to_df(SL_total_conversion_hour))

    # Staff Sales
    staff1 = db.sql_to_df(SL_staff_day)
    staff1 = utils_bot.df_staff_sales_to_str(staff1)
    staff2 = db.sql_to_df(SL_staff_hour)
    staff2 =  utils_bot.df_staff_sales_to_str(staff2)
    message = f"""{date}\n
*TODAY'S CONVERSION:*\n
{today1}\n
{today2}\n
\n*HOUR CONVERSION:*\n
{hour1}\n
{hour2}\n
\n*STAFF SALES:*\n
*Today's Sales*
{staff1}\n
*Hour Sales*
{staff2}
"""
    logging.info(message)
    bot.send_message(GROUP_ID, message)

def send_sales_report(especial=False, test=False):
    if test:
        # For TEST
        GROUP_ID = os.getenv('TEST_GROUP')
    else:
        # Define chat id
        GROUP_ID = os.getenv('SALES_GROUP')


    
    try:
        NOW = pd.Timestamp.now()
        hour = NOW.hour
        logging.info('Bot online')
        # Time validation to check if the hour is between 6 and 21
        if (hour >= 6 and hour <= 21) or especial:
            main(GROUP_ID)
            logging.info('Process Successful')
        else:
            logging.info('Execution after hours')
    except Exception as e:
        logging.exception(e)
        return e
if __name__ == '__main__':
    send_sales_report(
        especial= True,
        test= True)
   