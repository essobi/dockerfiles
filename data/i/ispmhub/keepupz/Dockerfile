FROM python:3.5.2  
MAINTAINER vagner.guedes@ispm.com  
  
RUN mkdir -p /code/  
COPY receiver.py /code/receiver.py  
COPY pyZabbixSender.py /code/pyZabbixSender.py  
COPY zabbix_helpers.py /code/zabbix_helpers.py  
COPY tests.py /code/tests.py  
  
COPY requirements.txt /code/requirements.txt  
RUN pip install -r /code/requirements.txt  
  
WORKDIR /code  
CMD ["python", "receiver.py"]

