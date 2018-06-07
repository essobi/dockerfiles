FROM alpine:3.6  
MAINTAINER Lukasz Olszewski <lukasz.olszewski@fastwhitecat.com>  
  
EXPOSE 80  
  
RUN apk update && \  
apk upgrade && \  
apk add varnish bash  
  
ADD start.sh /start.sh  
ADD varnish.vcl /etc/varnish/varnish.vcl  
ADD secret /etc/varnish/secret  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  

