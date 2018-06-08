################################################################################  
# DOCKER IMAGE BUILD FILE  
################################################################################  
FROM louiemenard/centos  
  
MAINTAINER Louie Menard <louie.menard@gmail.com>  
LABEL description="Vowpal Wabbit"  
LABEL version="1.0"  
  
################################################################################  
# install packages  
################################################################################  
USER root  
RUN yum install -y make  
RUN yum install -y automake  
RUN yum install -y autoconf  
RUN yum install -y clang  
RUN yum install -y boost  
RUN yum install -y boost-devel  
RUN yum install -y zlib  
RUN yum install -y zlib-devel  
RUN yum install -y libtool  
RUN yum install -y gcc  
RUN yum install -y gcc-c++  
  
################################################################################  
# install vw  
################################################################################  
WORKDIR /home/Louie  
RUN git clone https://github.com/JohnLangford/vowpal_wabbit.git  
WORKDIR vowpal_wabbit  
RUN ./autogen.sh  
RUN make  
#RUN make test  
RUN make install  
  
################################################################################  
# entry point  
################################################################################  
USER Louie  
WORKDIR /home/Louie  

