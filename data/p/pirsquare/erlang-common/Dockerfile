FROM centos:7  
MAINTAINER Ryan Liao <pirsquare.ryan@gmail.com>  
  
RUN yum -y update; \  
yum install -y wget tar xz xz-libs sudo gcc glibc-devel make ncurses-devel
openssl-devel \  
autoconf git make  
  
WORKDIR /opt  
  
RUN wget http://www.erlang.org/download/otp_src_18.1.tar.gz  
  
RUN tar zxvf otp_src_18.1.tar.gz && cd otp_src_18.1 \  
&& ./configure && make && make install  

