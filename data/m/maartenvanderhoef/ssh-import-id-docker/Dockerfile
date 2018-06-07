FROM jfloff/alpine-python  
  
RUN apk update && \  
apk add openssh && \  
pip install requests && \  
pip install ssh-import-id && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/ssh-import-id"]  

