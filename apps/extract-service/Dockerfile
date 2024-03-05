FROM python:3.10.13-alpine3.18

WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

WORKDIR /usr/src/app/app

CMD [ "python3", "main.py" ]