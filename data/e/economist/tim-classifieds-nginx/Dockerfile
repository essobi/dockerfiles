# Install from docker image CentOS 6  
FROM centos:centos6  
#The container is maintained from Cent OS  
MAINTAINER The CentOS Project <cloud-ops@centos.org>  
  
# Perform updates  
RUN yum -y update; yum clean all  
  
# Install EPEL for owncloud packages  
RUN yum -y install epel-release; yum clean all  
  
#Instaling simple nginx only  
RUN yum -y install nginx; yum clean all  
  
#Adding the site Content  
ADD nginx.conf /etc/nginx/  
ADD classifieds_dev.conf /etc/nginx/conf.d/  
ADD classifieds_prod.conf /etc/nginx/conf.d/  
ADD fastcgi_params /etc/nginx/  
RUN rm /etc/nginx/conf.d/default.conf  
  
RUN echo "upstream php-fpm { server php:9000; }" >
/etc/nginx/conf.d/upstream.conf  
  
# Expose port 80  
EXPOSE 80  
#Runnig the nginx  
CMD [ "/usr/sbin/nginx" ]

