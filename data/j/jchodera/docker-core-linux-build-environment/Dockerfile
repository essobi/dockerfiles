FROM centos:6.6  
# Install EPL  
ADD http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm .  
RUN rpm -i --quiet epel-release-6-8.noarch.rpm  
  
# Install prerequisites  
RUN yum install -y --quiet wget clang gcc gcc-c++ git scons redhat-lsb kernel-
devel dkms cmake doxygen  
  
# Install CUDA  
ENV CUDA_HOME=/usr/local/cuda-7.0 CUDA_LIBPATH=/usr/local/cuda-7.0/lib64  
ADD http://developer.download.nvidia.com/compute/cuda/repos/rhel6/x86_64/cuda-
repo-rhel6-7.0-28.x86_64.rpm .  
RUN rpm -i --quiet cuda-repo-rhel6-7.0-28.x86_64.rpm  
RUN yum clean expire-cache  
RUN yum install -y --quiet cuda  
  
# Install AMD SDK for OpenCL  
ENV OPENCL_HOME=/opt/AMDAPPSDK-2.9-1
OPENCL_LIBPATH=/opt/AMDAPPSDK-2.9-1/lib/x86_64  
ADD http://jenkins.choderalab.org/userContent/AMD-APP-SDK-
linux-v2.9-1.599.381-GA-x64.tar.bz2 .  
RUN tar xjf AMD-APP-SDK-linux-v2.9-1.599.381-GA-x64.tar.bz2  
RUN ./AMD-APP-SDK-v2.9-1.599.381-GA-linux64.sh -- -s -a yes  
  
# Get Boost  
ENV BOOST_PKG=boost_1_55_0 BOOST_SOURCE=$HOME/boost_1_55_0  
RUN wget --quiet
http://downloads.sourceforge.net/project/boost/boost/1.55.0/boost_1_55_0.tar.bz2  
RUN tar xjf $BOOST_PKG.tar.bz2 $BOOST_PKG/libs/regex
$BOOST_PKG/libs/filesystem $BOOST_PKG/libs/system $BOOST_PKG/libs/iostreams
$BOOST_PKG/boost  
  
# Build OpenSSL  
ENV OPENSSL_HOME=$HOME/openssl-1.0.2d  
RUN wget https://www.openssl.org/source/openssl-1.0.2d.tar.gz  
RUN tar zxf openssl-1.0.2d.tar.gz  
RUN cd openssl-1.0.2d ; ./config no-shared ; make  
  
# Build cbang  
ENV CBANG_HOME=$HOME/cbang  
RUN git clone \--depth=1 https://github.com/CauldronDevelopmentLLC/cbang.git  
RUN scons -C cbang  
  

