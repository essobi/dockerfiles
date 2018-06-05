FROM aurorasystem/server:latest  
MAINTAINER Aurora System <it@aurora-system>  
  
# Python3 and MKL  
RUN \  
yum install -y epel-release && yum install -y python34 && yum remove -y epel-
release && yum clean all && \  
ln -s /usr/bin/python3 /usr/local/bin/python3  
  
RUN yum install -y libcurl && yum install -y fftw && yum install -y wget &&
yum install -y git  
  
# cmake  
RUN cd /tmp && \  
wget https://cmake.org/files/v3.7/cmake-3.7.2.tar.gz && \  
tar -zxf cmake-3.7.2.tar.gz && cd cmake-3.7.2/ && \  
./bootstrap && make && make install && \  
rm -rf /tmp/*  
  
RUN yum install -y libcurl-devel  
  
# curlpp  
RUN cd /tmp && git clone -b master https://github.com/jpbarrette/curlpp.git &&
cd curlpp && \  
cmake CMakeLists.txt && make && make install && \  
rm -rf /tmp/*  
  
# jsoncpp  
RUN cd /tmp && git clone -b master https://github.com/open-source-
parsers/jsoncpp.git && cd jsoncpp && \  
cmake CMakeLists.txt && make && make install && \  
rm -rf /tmp/*  
  
# Python pip, numpy  
ADD ./get-pip.py /tmp  
RUN cd /tmp && \  
/usr/local/bin/python3 get-pip.py && \  
pip install numpy  
  
Add mkl_so/* /usr/local/lib/  

