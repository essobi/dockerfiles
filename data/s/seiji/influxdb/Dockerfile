FROM centos:centos6  
MAINTAINER Seiji Toyama <seijit@me.com>  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL C  
  
RUN rpm -Uvh http://ftp-
srv2.kddilabs.jp/Linux/distributions/fedora/epel/6/x86_64/epel-
release-6-8.noarch.rpm\  
&& yum -y upgrade  
  
RUN yum -y groupinstall "Development Tools"  
RUN yum -y install --enablerepo=centosplus\  
wget \  
&& yum -y clean all  
  
RUN cd /tmp && wget http://s3.amazonaws.com/influxdb/influxdb-
latest-1.x86_64.rpm \  
&& rpm -ivh influxdb-latest-1.x86_64.rpm  
  
ADD opt/influxdb/shared/config.toml /opt/influxdb/shared/  
EXPOSE 8083 8086 8099  
CMD
["/usr/bin/influxdb","-pidfile","/opt/influxdb/shared/influxdb.pid","-config","/opt/influxdb/shared/config.toml"]  

