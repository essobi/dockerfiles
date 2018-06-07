FROM centos:5.11  
MAINTAINER Lacour Maxime <contact@lacour-maxime.fr  
  
# install httpd  
RUN yum -y install httpd bash-completion unzip  
  
# install mysql  
RUN yum install -y mysql mysql-server  
RUN echo "NETWORKING=yes" > /etc/sysconfig/network  
  
# install php  
RUN yum install -y php php-mysql php-devel php-gd php-pecl-memcache php-pspell
php-snmp php-xmlrpc php-xml  
  
ADD run.sh ./  
RUN chmod +x run.sh  
  
CMD ["/run.sh"]  

