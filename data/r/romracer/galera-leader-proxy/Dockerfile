FROM alpine:3.4  
RUN apk add --update --no-cache bash socat  
ADD ./run.sh /  
  
ENTRYPOINT ["/run.sh"]  

