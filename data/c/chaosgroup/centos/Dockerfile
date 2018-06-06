FROM mlazarov/centos:6.4  
MAINTAINER Martin Lazarov <martin@lazarov.bg>  
  
RUN wget http://people.centos.org/tru/devtools-2/devtools-2.repo -O
/etc/yum.repos.d/devtools-2.repo  
RUN yum install -y vim patch git devtoolset-2-gcc devtoolset-2-binutils
devtoolset-2-gcc-c++ && yum clean all && scl enable devtoolset-2 bash  
ENV PATH $PATH:/opt/rh/devtoolset-2/root/usr/bin/  
  
CMD ["/bin/bash"]  

