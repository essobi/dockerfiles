#Install Apache on Centos7 with PHP  
# FROM project42/s6-centos-php  
FROM project42/s6-centos:centos7  
MAINTAINER Brandon Cone bcone@esu10.org  
  
#https://wordpress.org/latest.tar.gz  
COPY container-files /  
  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm \  
&& rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
RUN yum -y install httpd mod_ssl php56w php56w-cli php56w-soap php56w-xml yum
clean all  
  
EXPOSE 80  
# EXPOSE 443

