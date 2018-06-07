FROM debian  
MAINTAINER Fran Fariña <farinajf@gmail.com>  
  
RUN apt-get update && apt-get clean  
RUN apt-get install -y nginx && apt-get clean  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN echo "Nginx on Debian" > /usr/share/nginx/html/index.html  
  
EXPOSE 80  
CMD [ "/usr/sbin/nginx" ]  
  

