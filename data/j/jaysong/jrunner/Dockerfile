FROM java:8-jre-alpine  
  
RUN apk upgrade --update && \  
apk add --update bash && \  
rm -rf /tmp/* /var/cache/apk/*  
  
VOLUME ["/app", "/data"]  
WORKDIR /app  
  
CMD ["/bin/bash"]  

