FROM python:3.9

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY . /
WORKDIR /

EXPOSE 7000

CMD ["appp","app.py", "--server.port=7000"]
