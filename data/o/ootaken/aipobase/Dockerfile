FROM centos  
MAINTAINER Kenichiro Ota <oota_ken@hotmail.com>  
  
RUN yum update -y  
RUN yum install -y gcc nmap lsof unzip readline-devel zlib-devel git
java-1.8.0-openjdk-devel.x86_64 maven ruby rake sudo make iproute  
  
RUN yum -y update && yum clean all  
# set locale  
RUN yum reinstall -y glibc-common && yum clean all  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:ja  
ENV LC_ALL ja_JP.UTF-8  
RUN rm /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Japan /etc/localtime  
  
USER $CONTAINER_UID  

