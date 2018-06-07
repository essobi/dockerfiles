FROM centos:latest  
MAINTAINER xfsuper@gmail.com, https://github.com/linuxdict/docker  
  
RUN yum install -y ruby-devel gcc make rpm-build && gem install fpm && \  
yum remove -y gcc make cpp glibc-devel glibc-headers kernel-headers libgomp
mpfr && \  
yum clean all && \  
mkdir /build  
  
VOLUME ["/build"]  
  
WORKDIR /build  

