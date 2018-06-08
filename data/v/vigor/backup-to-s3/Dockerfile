FROM debian:jessie  
MAINTAINER DevOps <devops@vigorsystemsinc.com>  
  
RUN apt-get update && \  
apt-get install -y python wget unzip cron && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip && \  
unzip awscli-bundle.zip && \  
awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \  
mkdir /root/.aws/  
  
ADD credentials /root/.aws/credentials  
ADD config /root/.aws/config  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  
CMD [""]  

