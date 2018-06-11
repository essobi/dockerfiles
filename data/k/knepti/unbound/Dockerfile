FROM alpine:latest  
  
MAINTAINER knepti <knepti@gmail.com>  
  
RUN apk add --no-cache unbound  
  
ADD local.conf /etc/unbound/unbound.conf  
  
EXPOSE 53  
EXPOSE 53/udp  
  
ENTRYPOINT ["unbound"]  
  
CMD ["-d"]  

