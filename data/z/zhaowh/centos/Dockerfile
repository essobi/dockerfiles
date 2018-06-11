FROM centos:latest  
MAINTAINER Zhao Weihong  
  
RUN yum install -y wget && yum clean all  
  
#add yum source mirror  
RUN mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-
Base.repo.backup && \  
cd /etc/yum.repos.d/ && \  
wget -O /etc/yum.repos.d/CentOS-Base.repo
http://mirrors.aliyun.com/repo/Centos-6.repo  
  
#install epel  
RUN yum localinstall -y http://mirrors.aliyun.com/epel/6/x86_64/epel-
release-6-8.noarch.rpm && \  
rm /var/tmp/* -rf && yum clean all  
  
#add epel source mirror  
RUN mv /etc/yum.repos.d/epel.repo /etc/yum.repos.d/epel.repo.backup && \  
mv /etc/yum.repos.d/epel-testing.repo /etc/yum.repos.d/epel-
testing.repo.backup && \  
cd /etc/yum.repos.d/ && \  
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-6.repo  
  
#install tools  
RUN yum update -y && \  
yum install -y --enablerepo=epel \  
unzip \  
tar &&\  
yum clean all  
  
CMD ["bash"]  

