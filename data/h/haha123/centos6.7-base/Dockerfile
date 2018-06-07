FROM centos:centos6.7  
#RUN rm -rf /etc/yum.repos.d/*  
#ADD http://mirrors.163.com/.help/CentOS6-Base-163.repo
/etc/yum.repos.d/CentOS-Base.repo  
RUN \  
yum makecache && \  
yum -y install pcre-devel  
  
CMD ["bash"]  

