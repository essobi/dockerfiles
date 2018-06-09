FROM alpine:latest  
MAINTAINER playniuniu@gmail.com  
  
COPY nginx.conf /opt/nginx.conf  
  
RUN apk add --no-cache --update nginx \  
&& rm /etc/nginx/nginx.conf \  
&& mv /opt/nginx.conf /etc/nginx/  
  
VOLUME /opt/web/  
  
EXPOSE 80  
CMD ["/usr/sbin/nginx"]  
  

