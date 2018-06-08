FROM centos:latest  
MAINTAINER Antoine Petiteau petiteau@apc.in2p3.fr  
  
RUN yum -y update  
RUN yum install -y epel-release  
RUN yum install -y git  
RUN yum install -y make  
RUN yum install -y cmake  
RUN yum install -y fftw3-devel  
RUN yum install -y python-pip python-ipython numpy  
RUN yum install -y wget nano emacs  
RUN yum install -y gcc-gfortran.x86_64  
  
RUN pip install --upgrade pip  
  
ENV CXX c++  
  
WORKDIR /workspace  
RUN cd /workspace  
  
RUN mkdir /workspace/tools  
  
RUN wget http://pulsarastronomy.net/psrsoft/psrsoft.tar.gz  
RUN tar xvzf psrsoft.tar.gz  
RUN cp psrsoft/config/profile.example psrsoft/config/profile  
RUN mv psrsoft /workspace/tools/.  
ENV PSRSOFT_DIR /workspace/tools/psrsoft  
  
RUN cd /workspace  
  

