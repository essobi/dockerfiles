FROM alpine:3.1  
MAINTAINER Hans Donner <hans.donner@pobox.com>  
  
RUN apk add --update unbound openssl  
  
EXPOSE 53/udp  
  
CMD ["unbound", "-d"]  

