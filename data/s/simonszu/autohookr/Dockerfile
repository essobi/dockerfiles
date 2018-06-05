FROM python:alpine  
  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY hookr.py .  
COPY config.yaml .  
COPY crontab.txt /crontab.txt  
COPY run.sh /run.sh  
  
RUN mkdir /config \  
&& cp config.yaml /config \  
&& /usr/bin/crontab /crontab.txt \  
&& chmod 755 /run.sh  
  
ENTRYPOINT ["/run.sh"]

