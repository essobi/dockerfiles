FROM alpine:3.6  
MAINTAINER Achint Sandhu <sandhu@7theta.com>  
  
# Install docker  
RUN apk add --no-cache curl docker  
  
# Install docker-machine  
RUN curl -L
https://github.com/docker/machine/releases/download/v0.12.2/docker-machine-
Linux-x86_64 > /usr/local/bin/docker-machine && chmod +x
/usr/local/bin/docker-machine  
  
RUN apk del curl  
  
CMD ["sh"]  

