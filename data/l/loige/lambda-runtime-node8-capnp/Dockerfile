FROM loige/lambda-runtime-node8  
MAINTAINER Luciano Mammino <https://loige.co>  
  
# Install capnproto 0.6.1  
RUN curl -O https://capnproto.org/capnproto-c++-0.6.1.tar.gz && \  
tar zxf capnproto-c++-0.6.1.tar.gz && \  
cd capnproto-c++-0.6.1 && \  
./configure && \  
make -j6 check && \  
make install  
  
ENV LD_LIBRARY_PATH /var/task/lib  
  
RUN yum install -y sudo && yum clean all  

