import os

env_vars = {
# Project folder
'MAIN_PATH' : 'FunctionReportSales',

# Telegram API
'API_KEY' : "5259918785:AAGGOGWjFMC_8fRxKYTNcZtKQPfp9CZIGTI",
'TEST_GROUP' : '-1001730765313',
'SALES_GROUP' : '-1001570322854',

# Database
'SERVER' : 'tcp:soterlive1.database.windows.net.',
'DATABASE' : 'Soter_live',
'USER_NAME' : 'tylerzipfell',
'DATABASE_PASSWORD' : 'S0t3rTyl3r'

}

def load_env():
    for key, val in env_vars.items():
        os.environ[key] = val

load_env()
