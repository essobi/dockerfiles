FROM alpine  
RUN apk update && apk add netcat-openbsd  
ADD . /data  
RUN chmod +x /data/wait  
ENTRYPOINT ["/data/wait"]  

