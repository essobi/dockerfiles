FROM piuma/centos7-apache-php  
  
MAINTAINER Piuma <piuma@piumalab.org>  
  
RUN yum install -y \  
tar \  
&& rm -rf /var/cache/yum/* \  
&& yum clean all  
  
# install phpSysInfo version: v3.2.2  
RUN curl https://codeload.github.com/phpsysinfo/phpsysinfo/tar.gz/v3.2.2 \  
| tar xz --strip-components=1 -C /var/www/html \  
&& mv /var/www/html/phpsysinfo.ini.new /var/www/html/phpsysinfo.ini  
  
EXPOSE 80  
CMD /usr/sbin/httpd -c "ErrorLog /dev/stdout" -DFOREGROUND  

