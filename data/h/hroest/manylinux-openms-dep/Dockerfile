FROM quay.io/pypa/manylinux1_x86_64  
  
RUN wget --no-check-certificate http://cmake.org/files/v3.9/cmake-3.9.0.tar.gz  
RUN tar xzvf cmake-3.9.0.tar.gz  
WORKDIR /cmake-3.9.0  
RUN ./bootstrap  
RUN make  
RUN make install  
WORKDIR /  
  
RUN yum install -y libtool  
RUN yum install -y qt4 qt4-devel qt4-webkit-devel libzip-devel zlib-devel
bzip2-devel  
  
RUN git clone https://github.com/OpenMS/contrib.git  
RUN mkdir contrib-build  
  
WORKDIR /contrib-build  
  
RUN cmake -DBUILD_TYPE=ALL ../contrib  
  
WORKDIR /  
  

