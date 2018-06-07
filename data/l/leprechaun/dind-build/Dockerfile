FROM docker:stable-dind  
  
RUN apk update && apk add tree bash  
  
ADD docker-build.sh /usr/local/bin/docker-build  
RUN chmod 755 /usr/local/bin/docker-build  
  
ENTRYPOINT ["docker-build"]  

