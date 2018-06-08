FROM ubuntu:14.04  
MAINTAINER jsonfry  
  
RUN apt-get update && \  
apt-get install -y cron wget python-setuptools unzip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget https://github.com/s3tools/s3cmd/archive/master.zip && \  
unzip master.zip && \  
cd s3cmd-master/ && \  
python setup.py install  
  
ADD s3cfg /root/.s3cfg  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  

