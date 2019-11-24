FROM python:3.7-stretch
WORKDIR /code


# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt


RUN pip install pipenv
COPY Pipfile Pipfile
RUN pipenv install

CMD ["pipenv", "run", "python", "run.py"]
