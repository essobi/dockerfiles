FROM sebp/elk:562  
# Update apt-get  
RUN apt-get update  
# Install pip  
RUN apt-get install -y python-pip  
# Upgrade  
RUN pip install --upgrade pip  
# Install ES Curator with pip  
RUN pip install elasticsearch-curator  
# Cleaning  
RUN apt-get autoclean  
  
# Overwrite existing file  
COPY logstash/conf.d/* /etc/logstash/conf.d/  
  
# Copy curator config  
COPY curator/*.yml /etc/curator/  
# Copy curator runner  
COPY curator/run-curator.sh /bin/run-curator  
RUN chmod +x /bin/run-curator  
  
# Copy CRON  
COPY cron.d/* /etc/cron.d/  

