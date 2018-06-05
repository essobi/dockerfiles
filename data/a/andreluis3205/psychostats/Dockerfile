FROM centos:7  
MAINTAINER Andre Luis <andre@netbits.com.br>  
RUN \  
yum -y update \  
&& yum -y install --setopt=tsflags=nodocs \  
gd gd-devel cronie \  
wget \  
curl \  
nano \  
php \  
php-gd \  
php-mysql \  
mod_ssl \  
less \  
which \  
&& yum clean all \  
&& sed -ri 's/#ServerName www.example.com:80/ServerName localhost:80/g'
/etc/httpd/conf/httpd.conf \  
&& sed -ri 's/AllowOverride None/AllowOverride All/g'
/etc/httpd/conf/httpd.conf \  
&& sed -ri -e 's!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g' \  
-e 's!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g' \  
/etc/httpd/conf/httpd.conf  
RUN yum -y install epel-release  
RUN yum -y install php-mcrypt  
RUN yum -y install perl-DBD-MySQL  
  
COPY webmin.repo /etc/yum.repos.d/webmin.repo  
RUN wget http://www.webmin.com/jcameron-key.asc  
RUN rpm --import jcameron-key.asc  
#RUN yum -y install webmin  
#EXPOSE 10000  
#RUN echo -e "147852369\147852369" | passwd root  
#RUN systemctl enable crond.service  
#COPY crontab /etc/  
ADD index.php /var/www/html  
WORKDIR /var/www/html  
EXPOSE 80  
EXPOSE 10000  
ADD run-httpd.sh /run-httpd.sh  
RUN chmod -v +x /run-httpd.sh  
  
CMD ["/run-httpd.sh"]  

