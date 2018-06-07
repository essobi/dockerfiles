FROM centos:5  
MAINTAINER michimau <mauro.michielon@eea.europa.eu>  
  
COPY utter-ramblings.repo /etc/yum.repos.d/utter-ramblings.repo  
  
RUN yum -y update && yum -y install \  
httpd \  
php \  
php-mysql \  
php-ldap \  
php-xsl \  
vim \  
wget  
  
RUN wget -c http://dl.fedoraproject.org/pub/epel/5/x86_64/epel-
release-5-4.noarch.rpm && rpm -ivh epel-release-5-4.noarch.rpm  
  
RUN yum -y install ssmtp  
  
ADD ssmtp.conf /etc/ssmtp/ssmtp.conf  
  
COPY default /etc/httpd/conf.d/vh-iris2.conf  
  
EXPOSE 80  
CMD /usr/sbin/apachectl -D FOREGROUND  

