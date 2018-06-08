# Image from Alpine  
FROM alpine:latest  
  
# WebGenerators  
MAINTAINER Bence Sipos <sipimokus@gmail.com>  
  
# Install forwarder and clear cache  
RUN apk --update add bash socat \  
&& rm -rf /var/cache/apk/*  
  
# Settings  
ADD scripts/forward.sh /forward.sh  
RUN chmod +x /forward.sh  
  
# Start  
ENTRYPOINT [ "/forward.sh" ]  

