FROM centos:7  
# system update  
RUN yum -y update && yum clean all  
  
# set locale  
RUN yum reinstall -y glibc-common && yum clean all  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:ja  
ENV LC_ALL ja_JP.UTF-8  
RUN unlink /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Japan /etc/localtime  
  
# editor install  
RUN yum install -y vim && yum clean all  
  
# test  
ADD ./www/ /var/www/  

