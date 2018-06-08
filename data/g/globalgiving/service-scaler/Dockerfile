FROM alpine:3.7  
RUN apk add --update bash ca-certificates jq groff python3 curl \  
&& pip3 install awscli \  
&& rm -rf /var/cache/apk/*  
RUN mkdir -p /usr/docker /var/log/docker/  
ADD crontab.txt /usr/docker/crontab.txt  
ADD scaler.sh /usr/bin/  
COPY entry.sh /entry.sh  
RUN chmod 755 /entry.sh /usr/bin/scaler.sh  
RUN /usr/bin/crontab /usr/docker/crontab.txt  
CMD ["/entry.sh"]  

