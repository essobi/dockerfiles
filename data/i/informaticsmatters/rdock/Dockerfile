FROM centos:7  
MAINTAINER Tim Dudgeon  
  
RUN yum -y install epel-release && yum -y update &&\  
yum -y install gcc gcc-c++ make cppunit cppunit-devel popt popt-devel curl zip
unzip\  
numpy python-configparser openbabel openbabel-devel python-openbabel python-
pip &&\  
yum clean all  
  
ENV RBT_FILE rDock_2013.1_src  
ENV RBT_ROOT /$RBT_FILE  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:$RBT_ROOT/lib  
ENV PATH $PATH:$RBT_ROOT/bin  
  
COPY rDock_2013.1_src /rDock_2013.1_src  
  
WORKDIR /rDock_2013.1_src/build  
  
RUN cd $RBT_ROOT/build/ && make linux-g++-64 && make clean  
  
#RUN useradd -m rdock  
#USER rdock  
#WORKDIR /home/rdock  

