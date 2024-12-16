FROM python:3.12.8-alpine3.21

WORKDIR /helloworld

COPY . /helloworld

RUN pip install -r requirements.txt

CMD ["flask", "--app", "helloworld", "run", "--host", "0.0.0.0"]
