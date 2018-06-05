FROM alpine:edge  
  
MAINTAINER Jens Piegsa <piegsa@gmail.com>  
  
ADD eternal-fortune.sh /  
  
RUN apk update && \  
apk add --no-cache fortune && \  
chmod +x eternal-fortune.sh  
  
ENTRYPOINT ["/eternal-fortune.sh"]  
  

