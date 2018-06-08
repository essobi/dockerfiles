FROM alpine:latest  
  
MAINTAINER Gareth Munro  
  
RUN apk update && \  
apk add bash openssh-client rsync && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/bin/bash"]  

