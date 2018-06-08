FROM nitra/centos7  
  
MAINTAINER Nitra  
  
# import GPG signing key  
ADD RPM-GPG-KEY-nginx /etc/pki/rpm-gpg/RPM-GPG-KEY-nginx  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-nginx  
# install package  
ADD nginx-mainline.repo /etc/yum.repos.d/nginx-mainline.repo  
RUN yum install -y nginx psmisc  
ADD vhost.conf /etc/nginx/conf.d/default.conf  
RUN sed -i "s/worker_processes.*/worker_processes 4;/" /etc/nginx/nginx.conf
&& \  
sed -i "28i\client_max_body_size 50m;" /etc/nginx/nginx.conf && \  
sed -i "29i\gzip on;" /etc/nginx/nginx.conf && \  
sed -i "30i\gzip_disable "msie6";" /etc/nginx/nginx.conf && \  
sed -i "31i\gzip_vary on;" /etc/nginx/nginx.conf && \  
sed -i "32i\gzip_proxied any;" /etc/nginx/nginx.conf && \  
sed -i "33i\gzip_comp_level 6;" /etc/nginx/nginx.conf && \  
sed -i "34i\gzip_buffers 16 8k;" /etc/nginx/nginx.conf && \  
sed -i "35i\server_tokens off;" /etc/nginx/nginx.conf && \  
sed -i "36i\gzip_types text/plain text/css application/json
application/x-javascript text/xml application/xml application/xml+rss
text/javascript application/javascript;" /etc/nginx/nginx.conf  
#add locale  
RUN rm -rf /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Kiev /etc/localtime  
### Add autostart script  
ADD start.sh /start.sh  
ADD nginx_restart.sh /nginx_restart.sh  
RUN chmod +x /start.sh /nginx_restart.sh  
RUN ln -s /nginx_restart.sh /usr/bin/nginx_restart  
WORKDIR /etc/nginx/conf.d  
# Endpoint  
CMD ["/start.sh"]  
  

