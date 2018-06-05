FROM alpine  
  
MAINTAINER Lycreal <jgsly123@gmail.com>  
  
RUN apk add --no-cache openssh curl  
  
COPY entrypoint.sh /entrypoint  
  
RUN chmod +x /entrypoint  
  
EXPOSE 22  
ENTRYPOINT ["/entrypoint"]  

