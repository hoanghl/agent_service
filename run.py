import app.settings as settings

from app import app

if settings.ENV == "DEV":
    app.run(debug=True, host="0.0.0.0", port=settings.ACCESS_PORT)
elif settings.ENV == "PROD":
    app.run(debug=False, host="0.0.0.0", port=settings.ACCESS_PORT)
else:
    print("Bad ENV")
    exit(1)
    