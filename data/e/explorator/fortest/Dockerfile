# Nginx  
#  
# VERSION 0.0.4  
FROM centos:6.6  
MAINTAINER Fortest <fortest@gor.com>  
  
LABEL Description="This image is used to start the foobar executable"
Vendor="ACME Products" Version="1.1"  
  
RUN rpm -ivh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum -y update  
RUN yum -y install nano openssh-server wget perl tar exim rsyslog crontabs zip
bzip2 httpd php php-gd php-xml php-mcrypt php-pdo php-mysql php-bcmath php-
tidy php-tcpdf php-pear GeoIP dovecot proftpd mysql-server bind squirrelmail
awstats phpMyAdmin procmail mod_ssl cyrus-sasl cyrus-sasl-plain cyrus-sasl-md5
quota  
RUN chkconfig sshd on  
RUN chkconfig dovecot on  
RUN chkconfig exim on  
RUN chkconfig httpd on  
RUN chkconfig mysqld on  
RUN chkconfig named on  
RUN chkconfig proftpd on  
  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
ENV AUTHORIZED_KEYS **None**  
  
EXPOSE 21 22 25 53 80 110 143 443 465 1500 3306  
CMD ["/run.sh"]  

