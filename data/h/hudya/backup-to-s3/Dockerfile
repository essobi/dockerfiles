FROM alpine  
MAINTAINER <evin@napsty.com>  
  
RUN apk update && \  
apk add py-pip apk-cron curl openssl bash && \  
pip install -U pip && \  
pip install awscli && \  
rm -rf /var/cache/apk/*  
  
ADD app /app  
  
ENTRYPOINT ["/app/start.sh"]  

