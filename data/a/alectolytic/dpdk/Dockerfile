FROM cloudrouter/base-centos:latest  
MAINTAINER arun.neelicattu@gmail.com  
  
LABEL RUN docker run -it --privileged -v
/sys/bus/pci/drivers:/sys/bus/pci/drivers -v
/sys/kernel/mm/hugepages:/sys/kernel/mm/hugepages -v
/sys/devices/system/node:/sys/devices/system/node -v /dev:/dev --name NAME -e
NAME=NAME -e IMAGE=IMAGE IMAGE  
  
RUN yum -y upgrade  
RUN yum -y install dpdk  
RUN yum -y clean all  
  
CMD ["/usr/bin/bash"]  
  
ONBUILD RUN yum -y upgrade && yum -y clean all  

