FROM alpine:3.4  
RUN adduser -DH nc_semantics && \  
apk update && apk upgrade && \  
apk add --no-cache python py-pip py-flask uwsgi-python && \  
pip install --no-cache-dir pattern && \  
rm /var/cache/apk/*  
  
WORKDIR /etc/uwsgi  
COPY sentiment.py sentiment.ini /etc/uwsgi/  
  
ENTRYPOINT ["uwsgi", "--ini", "/etc/uwsgi/sentiment.ini"]  

