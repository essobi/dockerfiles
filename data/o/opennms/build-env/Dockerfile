FROM opennms/maven:latest  
  
LABEL maintainer "Ronny Trommer <ronny@opennms.org>"  
  
ARG
NSIS_RPM_URL="http://yum.opennms.org/stable/rhel7/nsis/mingw32-nsis-2.50-1.el7.centos.x86_64.rpm"  
RUN yum -y \--setopt=tsflags=nodocs update && \  
yum -y install git \  
which \  
expect \  
make \  
cmake \  
gcc-c++ \  
rrdtool-devel \  
automake \  
libtool \  
rpm-build \  
redhat-rpm-config \  
${NSIS_RPM_URL} && \  
yum clean all && \  
rm -rf /var/cache/yum  
  
RUN useradd -m circleci  
  
USER circleci  

