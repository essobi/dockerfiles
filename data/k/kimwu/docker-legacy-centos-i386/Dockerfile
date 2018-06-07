FROM centos:centos5  
MAINTAINER Kim Wu <kimwu@live.hk>  
  
# Env setup  
ENV HOME /root  
  
# install & link compat libs  
RUN yum -y update && \  
yum -y install glibc.i686 expat-devel.i386 libstdc++.i386 openssl-devel.i386
libgcc.i386 compat-libstdc++-296.i386 && \  
yum -y clean all && \  
ln -s /usr/lib/libstdc++-3-libc6.2-2-2.10.0.so
/usr/lib/libstdc++-libc6.2-2.so.2 && \  
ln -s /usr/lib/libstdc++-3-libc6.2-2-2.10.0.so
/usr/lib/libstdc++-libc6.1-1.so.2  
  
CMD ["/bin/bash"]  
  

