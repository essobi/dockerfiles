FROM centos:latest  
  
MAINTAINER Aleksey Tarasov <dark.ffh@gmail.com>  
  
RUN timedatectl set-timezone 'Europe/Moscow'; curl 'https://setup.ius.io/' |
bash  
  
#install gosu  
COPY gosu-install.sh /usr/local/bin/gosu-install.sh  
RUN bash /usr/local/bin/gosu-install.sh; rm /usr/local/bin/gosu-install.sh  
  
# update && install packages  
RUN yum -y update \  
&& yum -y install ansible ca-certificates wget pwgen dpkg nano \  
&& yum -y clean all  
  
CMD ["bash"]  

