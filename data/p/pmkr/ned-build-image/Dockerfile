FROM docker:1.12.2  
RUN \  
apk update && \  
apk add nodejs=6.2.0-r0  
  
RUN npm install -g ned-build-image@0.0.2  
  
WORKDIR /app  
  
ENTRYPOINT ["docker-entrypoint.sh", "ned-build-image"]  

