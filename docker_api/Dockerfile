FROM python:3

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "test.py" ]












# FROM python:3

# COPY ./requirements.txt /app/requirements.txt

# WORKDIR /app

# RUN pip3 install -r requirements.txt

# COPY . /app

# ENTRYPOINT [ "python3" ]

# CMD [ "api.py" ]



