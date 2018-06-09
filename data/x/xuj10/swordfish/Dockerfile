FROM java:8-jre-alpine  
  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
  
ADD build/install/swordfish/ /opt/swordfish/  
  
CMD ["/bin/bash", "/opt/swordfish/bin/swordfish"]  

