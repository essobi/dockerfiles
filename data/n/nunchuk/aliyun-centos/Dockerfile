############################################################  
# Dockerfile to build CentOS image for aliyun ecs  
# Based on CentOS:6.8  
############################################################  
  
FROM centos:6  
MAINTAINER XinYe <nunchuk@live.com>  
  
# Backup  
#RUN sed -i.backup 's/^enabled=1/enabled=0/'
/etc/yum/pluginconf.d/fastestmirror.conf  
RUN mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-
Base.repo.backup  
  
# Add ali-osm repo file  
#wget --quiet -O - /etc/yum.repos.d/CentOS-Base.repo
http://mirrors.aliyun.com/repo/Centos-6.repo  
#wget -qO /etc/yum.repos.d/epel.repo
http://mirrors.aliyun.com/repo/epel-6.repo  
COPY Centos-6.repo /etc/yum.repos.d/CentOS-Base.repo  
COPY epel-6.repo /etc/yum.repos.d/epel.repo  
  
# Update the repository and patch system  
RUN yum makecache \  
&& yum update bash glibc openssl wget ntp \  
&& rm -rf /var/cache/yum/*  
  
# Replace by aliyun ntp server  
COPY ntp.conf /etc/ntp.conf  
  
# change default time zone  
# ls -R --group-directories-first /usr/share/zoneinfo  
RUN rm /etc/localtime && ln -sf /usr/share/zoneinfo/Asia/Shanghai
/etc/localtime  
  
# change dns server  
RUN echo 'nameserver 223.5.5.5' >> /etc/resolv.conf

