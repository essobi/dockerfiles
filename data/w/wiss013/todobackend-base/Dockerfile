FROM centos:latest  
MAINTAINER BEN CHAABEN Wissem <benchaaben.wissem@gmail.com>  
  
#Prevent rpm errors  
ENV TERM=xterm-256color  
  
#set mirrors to NZ  
#RUN sed -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list  
RUN yum update && \  
yum install -y \  
epel-release python python-virtualenv python-libs python-devel mariadb-devel
MySQL-python  
  
# Create virtual envirement  
#Upgrate PIP in virtual envirement to latest version  
RUN virtualenv /appenv && \  
. /appenv/bin/activate && \  
pip install pip --upgrade  
  
# ADD entrypoint script  
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT [ "entrypoint.sh" ]  
LABEL application="todobackend"  

