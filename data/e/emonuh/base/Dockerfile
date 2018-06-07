FROM centos:7  
MAINTAINER emonuh  
  
# install basic commands  
RUN yum -y install curl-devel expat-devel gettext-devel openssl-devel zlib-
devel make gcc perl-ExtUtils-MakeMaker wget  
  
# install git  
RUN yum -y install git  
WORKDIR /usr/local/src  
RUN git clone git://git.kernel.org/pub/scm/git/git.git  
WORKDIR /usr/local/src/git  
RUN make prefix=/usr/local all  
RUN make prefix=/usr/local install  
RUN yum -y remove git  
  
# remove  
WORKDIR /root  
RUN rm -rf /usr/local/src/git  

