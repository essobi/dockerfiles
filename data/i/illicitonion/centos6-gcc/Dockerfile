FROM centos:6  
RUN yum -y update  
RUN yum install -y centos-release-scl  
RUN yum install -y \  
devtoolset-7-gcc \  
devtoolset-7-gcc-c++ \  
xz \  
m4 \  
libgcc.i686 \  
glibc-devel.i686  
  
# By default, execute in an environment with python27 enabled.  
ENTRYPOINT ["/usr/bin/scl", "enable", "devtoolset-7", "--"]  

