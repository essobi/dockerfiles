FROM busybox:latest  
  
ADD confd-0.11.0-linux-amd64 /usr/bin/confd  
ADD gncat /usr/bin/gncat  
RUN set -xe;\  
chmod +x /usr/bin/confd  
ENTRYPOINT ["confd"]  

