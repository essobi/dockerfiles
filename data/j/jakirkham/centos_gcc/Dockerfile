FROM centos:6.6  
MAINTAINER John Kirkham <jakirkham@gmail.com>  
  
  
RUN yum update -y && \  
yum install -y centos-release-scl && \  
yum install -y \  
devtoolset-4-gcc \  
devtoolset-4-gcc-c++ \  
devtoolset-4-gcc-gfortran && \  
yum clean all -y  
  
ENTRYPOINT ["scl", "enable", "devtoolset-4", "bash"]  

