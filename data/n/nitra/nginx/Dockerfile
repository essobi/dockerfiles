FROM centos:centos7  
  
MAINTAINER Nitra  
  
# import GPG signing key  
ADD etc/pki/rpm-gpg/RPM-GPG-KEY-nginx /etc/pki/rpm-gpg/RPM-GPG-KEY-nginx  
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-nginx  
  
# install package  
ADD etc/yum.repos.d/nginx-mainline.repo /etc/yum.repos.d/nginx-mainline.repo  
RUN yum install -y nginx vim  
  
ADD vhost.conf /etc/nginx/conf.d/default.conf  
ADD start.sh /start.sh  
RUN /bin/sed -i "29i\gzip on;" /etc/nginx/nginx.conf && \  
/bin/sed -i "30i\gzip_disable "msie6";" /etc/nginx/nginx.conf && \  
/bin/sed -i "31i\gzip_vary on;" /etc/nginx/nginx.conf && \  
/bin/sed -i "32i\gzip_proxied any;" /etc/nginx/nginx.conf && \  
/bin/sed -i "33i\gzip_comp_level 6;" /etc/nginx/nginx.conf && \  
/bin/sed -i "34i\gzip_buffers 16 8k;" /etc/nginx/nginx.conf && \  
/bin/sed -i "35i\gzip_types text/plain text/css application/json
application/x-javascript text/xml application/xml application/xml+rss
text/javascript;" /etc/nginx/nginx.conf  
  
# forward request logs to docker log collector  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
CMD /start.sh  

