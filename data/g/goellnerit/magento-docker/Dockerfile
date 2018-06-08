FROM centos:centos6  
MAINTAINER philipp@goellner.it  
RUN yum -y install wget  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum -y install which openssh-server php-mysql php-gd php-mcrypt php-zip
php-xml php-iconv php-curl php-soap php-simplexml php-pdo php-dom php-cli php-
fpm nginx  
RUN yum -y install tar mysql  
ADD default.conf /etc/nginx/conf.d/default.conf  
RUN chkconfig php-fpm on  
RUN chkconfig nginx on  
#install magento files  
ADD src /var/www  
RUN cd /var/www/ && chmod -R o+w media var && chmod o+w app/etc && chmod -R
o+w app/code/community/IntegerNet && chmod -R o+w
app/design/adminhtml/default/default/template && chmod -R o+w
app/code/community/ && chmod -R o+w app/design/frontend/base/default/template  
ADD mage-cache.xml /var/www/app/etc/mage-cache.xml  
  
ADD seturl.php /var/www/seturl.php  
RUN cd /var/www/ && wget
http://downloads3.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
&& tar xvfz ioncube_loaders_lin_x86-64.tar.gz  
ADD ZendGuardLoader.so /usr/lib64/php/modules/  
ADD ioncube_loader_lin_5.3.so /usr/lib64/php/modules/  
ADD ZendGuard.ini /etc/php.d/  
ADD start.sh /start.sh  
ADD 20-ioncube.ini /etc/php.d/  
RUN chmod 0755 /start.sh  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
CMD /start.sh  

