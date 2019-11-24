import app.settings as settings

def authenticate(request):
    '''Kiểm tra request có chứa password hợp lệ không

    :Args:
    - request - request mà client gửi lên
    
    :Rets:
    - True - nếu tồn tại trường `password` trong request và password hợp lệ
    - False - trường hợp còn lại
    '''
    if request.headers['password'] is None or request.headers['password'] != settings.ACCESS_KEY :
        return False
    else:
        return True

def reply_client(code, content):
    if code == 1:
        return "Incorrect password."
    elif code == 2:
        return "Incorrect data type."
    elif code == 3:
        return "Incorrect data format."
    elif code == 0:
        return content
    else:
        return "Unknown error."