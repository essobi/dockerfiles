FROM centos:7  
MAINTAINER mara <https://github.com/ma-ra/docker-centos7-apache>  
  
RUN rm /etc/localtime ; ln -s /usr/share/zoneinfo/Europe/Warsaw /etc/localtime  
  
RUN yum -y install httpd wget git  
RUN yum clean all  
  
ADD httpd.conf /etc/httpd/conf/httpd.conf  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod 550 /usr/local/bin/entrypoint.sh  
RUN touch /var/run/docker-container-creating  
  
EXPOSE 80  
#ENTRYPOINT ["/usr/sbin/httpd", "-DFOREGROUND"]  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

