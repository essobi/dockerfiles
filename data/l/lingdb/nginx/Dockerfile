FROM nginx:1.9.7  
MAINTAINER Jakob Runge <runjak@gmail.com>  
  
LABEL lingdb="nginx" \  
version="1.3.1" \  
documentation="https://github.com/lingdb/container/wiki/nginx"  
  
# To prevent DNS floods:  
# https://serverfault.com/a/345922/138127  
RUN echo "options single-request" >> /etc/resolv.conf  
  
# Copying config files:  
COPY siteconfig /etc/nginx/conf.d/default.conf  
COPY htpasswd /  
COPY ielexStatic /ielexStatic  

