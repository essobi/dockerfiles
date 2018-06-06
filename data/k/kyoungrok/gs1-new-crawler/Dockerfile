FROM python:2.7  
RUN apt-get update && apt-get install -y \  
supervisor \  
cron && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt  
COPY . /crawler  
WORKDIR /crawler  
RUN chmod -R +x /crawler && \  
pip install .  
  
ENTRYPOINT ["/bin/bash", "/crawler/scripts/run.sh"]  
CMD ["run"]  

