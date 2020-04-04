FROM python:3.7.7-slim
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -q -r /tmp/requirements.txt
ADD . /opt/app/
WORKDIR /opt/app
