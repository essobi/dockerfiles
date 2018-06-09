FROM alpine:3.3  
RUN apk add --update bash curl jq syslog-ng groff less python py-pip && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm -rf /var/cache/apk/*  
  
ADD onstart.sh /root/onstart.sh  
ADD syslog-ng.conf /root/syslog-ng.conf  
  
ENTRYPOINT ["/root/onstart.sh"]  

