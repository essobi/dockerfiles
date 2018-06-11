## Re-use tuleap base for caching ##  
FROM centos:centos6  
  
MAINTAINER Manuel Vacelet, manuel.vacelet@enalean.com  
  
RUN yum -y install php && yum clean all  
  
# Code coverage  
RUN rpm -i http://mir01.syntis.net/epel/6/i386/epel-release-6-8.noarch.rpm  
RUN yum -y install php-pecl-xdebug && yum clean all  
  
# Composer  
RUN yum -y install php-xml && yum clean all  
RUN curl -k -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin  
ADD composer.json /tmp/run/composer.json  
RUN cd /tmp/run && php /usr/local/bin/composer.phar install  
  
ADD run.sh /  
  
ENTRYPOINT [ "/run.sh" ]  
  
VOLUME ["/tuleap"]  

