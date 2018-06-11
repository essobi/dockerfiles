# ldapAdmin  
#  
# Web UI for LDAP server  
#  
FROM yuanzhencai/ci-base  
MAINTAINER Yuan Zhencai <zhencai.yuan@datarx.cn>  
  
EXPOSE 80  
RUN yum -y install phpldapadmin \  
&& yum -y clean all && rm -rf /var/cache/*  
  
COPY phpldapadmin/config.php /etc/phpldapadmin/  
COPY httpd/* /etc/httpd/conf.d/  
RUN chgrp apache /etc/phpldapadmin/config.php /etc/httpd/conf.d/*.conf \  
&& chmod 640 /etc/phpldapadmin/config.php /etc/httpd/conf.d/*.conf  
  
CMD ["apachectl", "-k", "start", "-DFOREGROUND"]  
  

