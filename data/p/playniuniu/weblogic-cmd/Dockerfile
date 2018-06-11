FROM alpine:latest  
MAINTAINER playniuniu@gmail.com  
  
WORKDIR /data  
COPY . /data  
  
RUN apk add --no-cache --update python3 py3-paramiko \  
&& rm -rf /var/cache/apk/*  
  
VOLUME /data  
  
ENTRYPOINT ["/data/command.py"]  
CMD ["-h"]  

