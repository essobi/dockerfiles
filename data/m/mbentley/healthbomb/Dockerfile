FROM alpine:latest  
MAINTAINER Matt Bentley <mbentley@mbentley.net>  
  
HEALTHCHECK \--retries=3 \--interval=5s \--timeout=3s CMD ps -ef | grep -v
grep | grep ping  
CMD ["ping","127.0.0.1"]  

