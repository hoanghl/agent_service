from flask import Blueprint, jsonify, request
import json

from app.modules.classify import classify
from app.misc import authenticate, reply_client
import app.resources as resources
import app.settings as settings

mod = Blueprint('api', __name__)

@mod.route('/agent', methods=['POST'])
def trigger_agent():
    # kiểm tra password
    if authenticate(request) is False:
        return reply_client(resources.RCODE_IPASS, "")

    # kiểm tra xem request gửi lên data có đang ở dạng JSON không
    if request.is_json:
        request_data = json.loads(request.data)

        # print(request_data.keys())

        if request_data['content'] is None:
            return reply_client(resources.RCODE_IDATTYP, "")
        else:
            if settings.ENV == "PROD":
                # try:
                #     if classify(request_data) == 1:
                #         return reply_client(resources.RCODE_IDATTYP, "Value of one or many attributes is incorrect.")
                #     else:
                #         return reply_client(resources.RCODE_DONE, "")
                # except Exception:
                #     return reply_client(resources.RCODE_IERROR, "")
                if classify(request_data) == 1:
                    return reply_client(resources.RCODE_IDATTYP, "Value of one or many attributes is incorrect.")
                else:
                    return reply_client(resources.RCODE_DONE, "")
            elif settings.ENV == "ENV":
                return reply_client(resources.RCODE_DONE, str(classify(request_data)))
            else:
                return reply_client(resources.RCODE_IERROR, "Bad ENV variable.")
    else:
        return reply_client(resources.RCODE_IDATTYP, "")
