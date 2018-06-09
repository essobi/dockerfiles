FROM centos:6.6  
MAINTAINER Sergey Tuchkin <tuchkin@gmail.com>  
RUN yum install -y createrepo which  
RUN mkdir -p /opt/yum-testing  
RUN createrepo /opt/yum-testing  
RUN { echo '[yum-testing]'; echo 'name = Yum Testing'; echo 'baseurl =
file:///opt/yum-testing'; echo 'gpgcheck = 0'; } >/etc/yum.repos.d/yum-
testing.repo  
RUN yum install -y java-1.8.0-openjdk.x86_64  
CMD /bin/bash  
  

