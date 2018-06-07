FROM gerasim13/flask-gunicorn  
COPY requirements.txt /tmp/  
RUN apk update  
RUN apk --update add build-base git ffmpeg-libs ffmpeg g++ sqlite sqlite-libs
sqlite-dev python3-dev  
RUN pip3 install -r /tmp/requirements.txt  
RUN apk del build-base python3-dev sqlite-dev && \  
rm -rf /root/.cache/pip/* && \  
rm -rf /var/cache/apk/* && \  
rm -rf /tmp/*  

