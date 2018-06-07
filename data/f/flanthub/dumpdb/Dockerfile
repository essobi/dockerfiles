FROM alpine:3.6  
RUN apk add --no-cache coreutils util-linux bash postgresql mysql-client  
COPY dump.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/dump.sh  
ENTRYPOINT ["/usr/local/bin/dump.sh"]  

