FROM alpine:latest  
  
MAINTAINER NI JIALIANG  
  
RUN apk --update add nginx python py-pip uwsgi uwsgi-python && \  
pip install --upgrade pip && \  
pip install flask supervisor requests  
  
ENTRYPOINT ["supervisord"]  
EXPOSE 80  

