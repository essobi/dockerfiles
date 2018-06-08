FROM java:openjdk-7-alpine  
MAINTAINER Raymond Kroon <raymond@k3n.nl>  
  
RUN apk add --update bash git && rm -rf /var/cache/apk/*  
RUN adduser -D -h /home/user user  
  
USER user  
WORKDIR /home/user  
  
#mount point for app  
WORKDIR /home/user/app  
VOLUME /home/user/app  
  
ENTRYPOINT ["java"]  

