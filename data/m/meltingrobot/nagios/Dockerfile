# Version 0.0.2  
FROM centos:latest  
MAINTAINER Roy P "meltingrobot@gmail.com"  
RUN yum -y update  
RUN yum -y install epel-release  
RUN yum -y install fping httpd mod_ssl nagios nagios-plugins-all postfix ||
true  
RUN touch /var/run/nagios.pid  
RUN chown nagios.nagios /var/run/nagios.pid  
RUN chmod u+s /usr/bin/ping  
RUN echo "Hello World" > /var/www/html/index.html || true  
RUN sed -i 's/inet_protocols = all/inet_protocols = ipv4/g'
/etc/postfix/main.cf  
RUN /usr/bin/newaliases  
RUN mkdir /root/bin  
RUN mkdir /var/log/nagios/rw  
RUN chown nagios.nagios /var/log/nagios/rw/  
RUN echo "RedirectMatch ^/$ /nagios/" >> /etc/httpd/conf/httpd.conf  
CMD [ "/bin/bash", "-c", "/usr/bin/yum -y
update;/usr/sbin/httpd;/usr/sbin/postfix start;/usr/sbin/nagios
/etc/nagios/nagios.cfg" ]  
VOLUME /etc/nagios  
VOLUME /var/spool/nagios  
VOLUME /etc/httpd  
EXPOSE 80  
EXPOSE 443  

