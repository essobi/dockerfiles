FROM fedora:22  
MAINTAINER Rino Rondan villadalmine@gmail.com  
  
RUN dnf -y update && dnf clean all  
RUN dnf -y install httpd && dnf clean all  
RUN rm -rf /run/httpd/* /tmp/httpd*  
ENV APACHE_RUN_USER apache  
ENV APACHE_RUN_GROUP apache  
ENV APACHE_LOG_DIR /var/log/httpd  
  
RUN chown -R apache:apache /var/www/  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/apachectl"]  
CMD ["-D", "FOREGROUND"]  

