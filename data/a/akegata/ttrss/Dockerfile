FROM centos:centos7  
MAINTAINER Martin Hovmöller  
  
RUN yum -y install git php php-mbstring php-mysql php-xml unzip  
  
ADD php.conf /etc/httpd/conf.d/  
ADD httpd.conf /etc/httpd/conf/  
  
WORKDIR /var/www/html/  
RUN git clone https://github.com/gothfox/Tiny-Tiny-RSS.git  
ADD config.php /var/www/html/Tiny-Tiny-RSS/config.php  
RUN git clone https://github.com/tribut/ttrss-videoframes.git; mv ttrss-
videoframes/videoframes Tiny-Tiny-RSS/plugins/; rm -r ttrss-videoframes  
RUN chown -R apache.apache /var/www/html/Tiny-Tiny-RSS  
ADD run.sh /tmp/  
  
CMD /tmp/run.sh && /usr/sbin/httpd && /usr/bin/php /var/www/html/Tiny-Tiny-
RSS/update.php --daemon  

