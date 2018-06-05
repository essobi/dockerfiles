FROM centos:centos6  
MAINTAINER David Bain <david@alteroo.com>  
  
RUN yum update -y  
RUN rpm -Uvh http://fedora.mirror.nexicom.net/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN yum install varnish -y  
ADD default.vcl /etc/varnish/default.vcl  
CMD varnishd -a :6081 -f /etc/varnish/default.vcl -F -s
file,/var/lib/varnish/varnish_storage.bin,100M  
#/etc/init.d/varnish start  
EXPOSE 6081

