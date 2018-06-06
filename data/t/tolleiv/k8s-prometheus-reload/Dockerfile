FROM alpine  
RUN apk add --no-cache curl  
COPY refresh.sh /usr/local/bin  
ENTRYPOINT ["/usr/local/bin/refresh.sh"]  

