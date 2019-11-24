import json
import os

try:
    ENV = os.environ['ENV']
    CONF_PATH = os.environ['CONF_PATH']
except KeyError:
    print("Bad ENV argument.")
    exit(1)

# ENV = "DEV"
# CONF_PATH = "../configs.json"

with open(CONF_PATH, "r") as f:
    config = json.load(f)

    ACCESS_KEY = config['service_info']['agent_service']['key']
    ACCESS_PORT = config['service_info']['agent_service']['port']
    f.close()


if ENV == "PROD":
    with open(CONF_PATH, "r") as f:
        config = json.load(f)

        POSTGRE_USER  = config['db_info']['POSTGRE_USER']
        POSTGRE_PASS  = config['db_info']['POSTGRE_PASS']
        POSTGRE_HOST  = config['db_info']['POSTGRE_HOST']
        POSTGRE_PORT  = config['db_info']['POSTGRE_PORT']
        POSTGRE_DB    = config['db_info']['POSTGRE_DB']
        POSTGRE_SCHEM = config['db_info']['POSTGRE_SCHEM']
        POSTGRE_TABLE = config['db_info']['POSTGRE_TABLE']

        # POSTGRE_USER  = "postgres"
        # POSTGRE_PASS  = "(lock133)"
        # POSTGRE_HOST  = "127.0.0.1"
        # POSTGRE_PORT  = "5432"
        # POSTGRE_DB    = "atomic"
        # POSTGRE_SCHEM = "public"
        # POSTGRE_TABLE = "post"

        f.close()
elif ENV == "DEV":
    POSTGRE_USER  = "postgres"
    POSTGRE_PASS  = "(lock133)"
    POSTGRE_HOST  = "127.0.0.1"
    POSTGRE_PORT  = "5432"
    POSTGRE_DB    = "atomic"
    POSTGRE_SCHEM = "public"
    POSTGRE_TABLE = "post"
# else:
#     print("Bad ENV argument.")
#     exit(1)
