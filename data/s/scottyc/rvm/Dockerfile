  
# Docker file for CentOS with RVM  
FROM centos:centos7  
  
MAINTAINER Scott Coulton "https://github.com/scotty-c/docker-rvm"  
ENV HOME /root  
  
#VOLUME ["/usr/local/"]  
CMD ["/bin/bash", "-l"]  
  
RUN yum -y install curl which tar  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3  
RUN \curl -sSL https://get.rvm.io | bash -s stable --ruby=2.0  
RUN source /usr/local/rvm/scripts/rvm  

