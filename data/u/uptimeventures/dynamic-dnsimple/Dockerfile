FROM
alpine:3.7@sha256:7df6db5aa61ae9480f52f0b3a06a140ab98d427f86d8d5de0bedab9b8df6b1c0  
MAINTAINER Nicholas Young <nyoung@uptime.ventures>  
  
COPY rootfs /  
RUN apk upgrade \--update --no-cache && \  
apk add \--update --no-cache curl && \  
chmod +x /etc/periodic/15m/dnscast && \  
chmod +x /usr/local/bin/dnscast && \  
chmod +x run.sh  
  
CMD ["sh", "run.sh"]  

