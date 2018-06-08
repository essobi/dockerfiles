FROM centos  
MAINTAINER Jon Dell  
RUN rpm -Uvh http://fedora.mirror.nexicom.net/epel/6/i386/epel-
release-6-8.noarch.rpm  
ADD hop5.repo /etc/yum.repos.d/hop5.repo  
RUN yum install -y hhvm  
VOLUME ["/var/www"]  
EXPOSE 9000  
CMD ["/usr/bin/hhvm", "-m", "server", "-vServer.Type=fastcgi",
"-vServer.Port=9000"]

