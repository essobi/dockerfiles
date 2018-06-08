#  
# Dockerfile for shogi-server  
#  
FROM centos:centos6  
  
# update system  
RUN rpm --import http://ftp.riken.jp/Linux/centos/RPM-GPG-KEY-CentOS-6  
RUN yum history new  
RUN yum update -y  
  
# install locale  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8  
  
# install packages  
RUN yum install -y ruby  
RUN yum install -y git  
  
# download shogi-server module  
RUN git clone git://git.sourceforge.jp/gitroot/shogi-server/shogi-server.git
/opt/shogi-server  
  
EXPOSE 4081  
ENTRYPOINT ["ruby", "/opt/shogi-server/shogi-server", "event1", "4081"]  

