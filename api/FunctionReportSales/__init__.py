import os
import sys
import logging
import azure.functions as func
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
# Define project main path
MAIN_FOLDER = os.getenv('MAIN_PATH')

sys.path.insert(0, os.path.join(os.getcwd(), os.path.join(MAIN_FOLDER, "src") ))

from . import sales


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    test = req.params.get('test')
    if not test:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            test = req_body.get('test')
            
    especial = req.params.get('especial')
    if not test:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            especial = req_body.get('especial')

    try:
        response = sales.send_sales_report(especial, test)
        message = f"Report send to Telegram Chat. This HTTP triggered function executed successfully.\n\nespecial={especial},\ntest={test}"
        if response:
            message = message + f"\n\n{response}"
        return  func.HttpResponse(message)
    except Exception as e:
        return func.HttpResponse(
             f"This HTTP triggered function FAIL successfully.\n\n{str(e)}",
             status_code=500
        )
