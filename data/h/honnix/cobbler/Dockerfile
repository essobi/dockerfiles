FROM centos:7  
MAINTAINER hxliang1982@gmail.com  
  
# pykickstart installed for `cobbler validateks`  
RUN yum -y install epel-release;\  
yum -y install file cobbler cobbler-web pykickstart;\  
yum clean all;\  
touch /etc/xinetd.d/rsync  
  
EXPOSE 80 443  
CMD httpd -k start && cobblerd -F  

