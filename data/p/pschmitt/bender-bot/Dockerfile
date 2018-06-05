FROM alpine:3.3  
COPY docker/start.sh /usr/bin/start.sh  
COPY requirements.txt /tmp/requirements.txt  
  
RUN apk --update add build-base python python-dev py-pip py-gunicorn curl git
\  
&& pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt  
  
VOLUME /app  
WORKDIR /app  
  
ENV PARAMS="--bind 0.0.0.0:8000 --access-logfile - --reload
bender.facebook.app:app"  
EXPOSE 8000  
ENTRYPOINT /usr/bin/start.sh  

