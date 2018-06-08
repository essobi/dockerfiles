#OpenOnload 201606-u1.2 Container on Centos 7.3  
FROM centos:7.3.1611  
MAINTAINER Patrick Dehkordi  
ADD http://www.openonload.org/download/openonload-201606-u1.2.tgz .  
RUN yum install -y net-tools wget which perl make bash libtool  
RUN yum install -y libpcap-devel python-devel valgrind-devel  
RUN yum install -y libgcc.i686 glibc-devel.i686 glibc-devel.x86_64  
RUN tar -zxvf openonload-201606-u1.2.tgz  

