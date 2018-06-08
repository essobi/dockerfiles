FROM gradle:jdk8-alpine  
  
# Dependencies  
USER root  
RUN apk update && apk add libstdc++ tini && rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/sbin/tini", "--", "gradle", "assemble"]  
  
# Copy project files  
COPY . .  
  

