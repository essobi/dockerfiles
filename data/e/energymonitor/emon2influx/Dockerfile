FROM python:3.6  
WORKDIR /usr/src/emon2influx  
VOLUME /usr/src/emon2influx/logs  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python-requests \  
cron  
  
COPY _support/run.sh ./  
RUN chmod +x run.sh  
  
COPY _support/crontab /etc/cron.d/emon2influx-cron  
RUN crontab /etc/cron.d/emon2influx-cron  
  
COPY _support/requirements.txt ./  
RUN pip3 install --no-cache-dir -r requirements.txt  
  
COPY app ./app  
COPY config ./config  
  
RUN chmod +x ./app/emon2influx.py  
  
CMD ["cron", "-f"]  

