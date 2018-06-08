FROM alpine  
MAINTAINER <gaieges@gmail.com>  
  
RUN apk update && \  
apk add -y py-pip apk-cron curl openssl bash && \  
pip install -U pip && \  
pip install awscli && \  
rm -rf /var/cache/apk/*  
  
ADD s3cfg /root/.s3cfg  
  
ADD start.sh /start.sh  
ADD backup.sh /backup.sh  
ADD restore.sh /restore.sh  
  
ENTRYPOINT ["/start.sh"]  

