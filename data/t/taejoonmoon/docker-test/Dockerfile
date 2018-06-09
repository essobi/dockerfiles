FROM centos:6  
MAINTAINER Foo Bar <foo@bar.com>  
  
#RUN apt-get update  
RUN yum install -y httpd  
RUN echo "test" > /var/www/html/index.html  
RUN chkconfig --level 345 httpd on  
#RUN service httpd start  
  
#RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
#RUN chown -R www-data:www-data /var/lib/nginx  
  
VOLUME ["/data"]  
#VOLUME ["/data", "/etc/nginx/site-enabled", "/var/log/nginx"]  
  
WORKDIR /etc/init.d  
#CMD service httpd start  
CMD /bin/bash  
  
  
#ADD entrypoint.sh /entrypoint.sh  
#RUN chmod +x /entrypoint.sh  
#ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
#EXPOSE 443  

