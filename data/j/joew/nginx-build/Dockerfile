FROM centos:6  
MAINTAINER "Joe Wagner" <joew@joew.net>  
  
# epel repo is needed for nginx  
RUN yum install -y epel-release  
RUN yum install -y nginx  
  
# Replacements for /etc/nginx/conf.d/default.conf:  
ADD https://raw.githubusercontent.com/joewww/nginx/master/conf/dev.conf
/tmp/dev.conf  
ADD https://raw.githubusercontent.com/joewww/nginx/master/conf/prod.conf
/tmp/prod.conf  
  
# Web content  
RUN mkdir /var/www  
ADD https://raw.githubusercontent.com/joewww/nginx/master/www/index.html
/var/www/index.html  
RUN chmod 644 /var/www/index.html  
  
# Map logs to stdout/err  
RUN touch /var/log/nginx/{access,error}.log  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ls -sf /dev/stderr /var/log/nginx/error.log  
  
# Use wrapper script to test env var (dev vs prod)  
ADD https://raw.githubusercontent.com/joewww/nginx/master/conf/start-nginx.sh
/start-nginx.sh  
  
RUN chmod +x start-nginx.sh  
RUN /start-nginx.sh  
  

