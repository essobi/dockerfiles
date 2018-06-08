FROM centos:7  
MAINTAINER Marco Cyriacks <marco@cyriacks.net>  
  
RUN yum -y upgrade  
RUN yum install -y epel-release git rpm-build rpmdevtools libstdc++-devel
gcc-c++ make  
RUN yum install -y qt5-qtbase-devel qt5-qtwebkit-devel qt5-qtsvg-devel
libmarkdown-devel  
  
# Set correct timezone  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Setup build env  
RUN useradd makerpm  
USER makerpm  
RUN rpmdev-setuptree  
  

