FROM centos:centos6  
MAINTAINER Steven Merrill <steven.merrill@gmail.com>  
  
ADD provision.sh /tmp/provision-vagrant-centos.sh  
RUN bash /tmp/provision-vagrant-centos.sh  
  
EXPOSE 22  
CMD ["/sbin/init"]  

