FROM ubuntu:16.04  
MAINTAINER Christopher De Vries <devries@idolstarastronomer.com>  
  
RUN apt-get update && apt-get install -y software-properties-common && apt-get
clean  
  
COPY nginx_signing.key /  
RUN apt-key add /nginx_signing.key  
  
RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >>
/etc/apt/sources.list  
RUN echo "deb-src http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >>
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y nginx && apt-get clean  
  
RUN sed "s/access_log\s*[^;]*/access_log \/dev\/stdout/g" -i
/etc/nginx/nginx.conf  
RUN sed "s/error_log\s*[^;]*/error_log \/dev\/stdout/g" -i
/etc/nginx/nginx.conf  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
VOLUME /usr/share/nginx/html  
VOLUME /etc/nginx/conf.d  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/nginx"]  

