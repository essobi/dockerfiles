FROM alpine:3.7  
COPY run.sh /run.sh  
RUN apk add --no-cache curl  
RUN chmod +x /run.sh  
ENTRYPOINT ["/run.sh"]

