FROM alpine:3.5  
RUN apk add --no-cache git bash openssh-client  
COPY ./run.sh /run.sh  
RUN chmod +x /run.sh  
ENTRYPOINT ["/run.sh"]  

