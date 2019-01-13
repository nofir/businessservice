FROM python:2.7
EXPOSE 5000

WORKDIR /app
ADD . /app

RUN python -m pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "main.py" ]