FROM alpine:latest  
RUN apk add --no-cache bash curl git openssh  
  
RUN mkdir /var/data  
RUN mkdir /root/.ssh  
VOLUME /var/data  
VOLUME /root/.ssh  
RUN chmod 700 /root/.ssh  
  
WORKDIR /var/data  

