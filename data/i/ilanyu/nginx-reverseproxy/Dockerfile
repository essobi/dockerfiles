FROM alpine:latest  
  
MAINTAINER ilanyu <lanyu19950316@gmail.com>  
  
ENV REVERSE_PROXY_URL http://idea.lanyus.com  
  
RUN apk update && apk upgrade && \  
apk add nginx && \  
rm -rf /var/cache/apk/*  
  
COPY default.conf /etc/nginx/conf.d  
  
COPY nginx.sh /usr/  
  
RUN chmod 0755 /usr/nginx.sh  
  
EXPOSE 80  
CMD ["/usr/nginx.sh"]  

