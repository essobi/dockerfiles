FROM alpine:latest  
MAINTAINER José Luis Salvador Rufo <salvador.joseluis@gmail.com>  
  
ADD
https://github.com/kelseyhightower/confd/releases/download/v0.15.0/confd-0.15.0-linux-
amd64 /usr/local/bin/confd  
  
RUN apk --no-cache add coreutils && \  
chmod +x /usr/local/bin/confd  
  
CMD ["confd"]  
  

