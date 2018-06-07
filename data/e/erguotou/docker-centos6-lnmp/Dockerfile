# Centos6 and lnmp environment  
FROM daocloud.io/centos:6  
MAINTAINER erguotou <erguotou525@gmail.com>  
  
# Change to 163 yum repo  
RUN yum -y install wget tar  
#RUN echo "Change to 163 repo"  
#RUN wget http://mirrors.163.com/.help/CentOS6-Base-163.repo  
#RUN mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-
Base.repo.bak  
#RUN mv CentOS6-Base-163.repo /etc/yum.repos.d/CentOS-Base.repo  
RUN wget http://mirrors.sohu.com/help/CentOS-Base-sohu.repo  
#RUN mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-
Base.repo.bak  
#RUN mv CentOS-Base-sohu.repo /etc/yum.repos.d/CentOS-Base.repo  
RUN echo "Repo changed"  
RUN yum clean all  
RUN yum makecache  
RUN yum update -y  
RUN echo "yum updated to 163 repo"  
  
# Get lnmp  
RUN echo "Get lnmp script"  
RUN cd /tmp && wget http://mirrors.linuxeye.com/lnmp-full.tar.gz && tar xzf
lnmp-full.tar.gz  
RUN echo "You need to install lnmp after build."  
  
# Write init.sh  
RUN touch init_lnmp.sh  
RUN echo cd /tmp/lnmp >> init_lnmp.sh  
RUN echo ./install.sh >> init_lnmp.sh  
RUN chmod 755 init_lnmp.sh  
  
EXPOSE 80 22  
# Welcome  
ENTRYPOINT bash -c ./init_lnmp.sh

