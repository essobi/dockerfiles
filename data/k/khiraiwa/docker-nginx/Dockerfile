FROM ubuntu:14.04.2  
MAINTAINER khiraiwa  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN ["apt-get", "update"]  
RUN ["apt-get", "install", "software-properties-common", "python-software-
properties", "-y"]  
RUN ["add-apt-repository", "-y", "ppa:nginx/stable"]  
RUN ["apt-get", "update"]  
RUN ["apt-get", "install", "nginx", "-y"]  
  
RUN ["chown", "-R", "www-data:www-data", "/etc/nginx"]  
RUN ["chown", "-R", "www-data:www-data", "/var/lib/nginx"]  
RUN ["chown", "-R", "www-data:www-data", "/var/log/nginx"]  
RUN ["chown", "-R", "www-data:www-data", "/usr/sbin/nginx"]  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD proxy.conf /etc/nginx/conf.d/proxy.conf  
ADD default /etc/nginx/sites-available/default  
  
# Mount data dir  
RUN ["mkdir", "-p", "/data_nginx/log/nginx"]  
RUN ["mkdir", "-p", "/data_nginx/cache/nginx/temp"]  
RUN ["mkdir", "-p", "/data_nginx/cache/nginx/mysite"]  
  
RUN ["chown", "-R", "www-data:www-data", "/data_nginx"]  
VOLUME ["/data_nginx"]  
  
EXPOSE 80  
CMD /usr/sbin/nginx -c /etc/nginx/nginx.conf && \  
tail -100f /data_nginx/log/nginx/access.log  

