FROM centos:latest  
MAINTAINER Carles Cortes Costa "carles@carles.cc"  
# ENV REFRESHED_AT 1015-07-18  
# INSTALLS NECESSARY PACKAGES  
RUN yum -y clean all  
RUN yum -y makecache  
RUN yum -y install httpd wget php php-pear php-cli php-common php-mysql php-
fpm php-JsonSchema php-jsonlint php-tidy gettext unzip php-xml php-mbstring
php-gd  
  
# DOWNLOADS WALLABAG AND PUTS IT IN THE DOCUMENTROOT  
RUN wget http://wllbg.org/latest -O /tmp/wallabag.zip  
RUN unzip -q /tmp/wallabag.zip -d /tmp  
RUN mv /tmp/wallabag*/* /var/www/html/  
RUN rm -rf /tmp/wallabag*  
  
#DOWNLOADS THE VENDOR.ZIP  
RUN wget -O /tmp/vendor.zip http://wllbg.org/vendor  
RUN unzip -q /tmp/vendor.zip -d /tmp  
RUN mv /tmp/vendor/ /var/www/html/  
RUN rm -rf /tmp/vendor*  
  
#CHANGE DOCUMENTROOT PERMISSIONS  
RUN chown -R apache: /var/www/html  
  
#EXPOSE PORT 80 TO THE OUTSIDE  
EXPOSE 80  
#ADDS THE APACHE CONF  
ADD conf/wallabag-carles-cc.conf /etc/httpd/conf.d/  
  
#ADDS THE WALLABAG CONF, USER:WALLABAG PASS:WALLABAG  
ADD conf/config.inc.php /var/www/html/inc/poche/  
  
# STARTS APACHE ON THE FOREGROND  
ENTRYPOINT /usr/sbin/httpd -DFOREGROUND  
  

