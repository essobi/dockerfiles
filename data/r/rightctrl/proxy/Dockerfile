FROM rightctrl/centos  
MAINTAINER RightCtrl <support@RightCtrl.com>  
#Virtual hosting  
RUN yum install -y epel-release httpd wget  
RUN mkdir /etc/httpd/sites-enabled  
ADD proxy.conf /etc/httpd/sites-enabled/proxy.conf  
RUN printf "IncludeOptional sites-enabled/proxy.conf" >>
/etc/httpd/conf/httpd.conf  
  
EXPOSE 80  
EXPOSE 443  
#RUN rm -rf /run/httpd/* /tmp/httpd*  
#CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]  
ADD run-httpd.sh /run-httpd.sh  
RUN chmod -v +x /run-httpd.sh  
CMD ["/run-httpd.sh"]  

