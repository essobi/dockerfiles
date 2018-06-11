FROM wangyuntao/dev  
MAINTAINER wyt <wyt.daily@gmail.com>  
  
ENV PATH $PATH:$DEV_DIR/opt/apache-maven-3.2.5/bin  
  
RUN \  
wget -O - \  
https://github.com/google/protobuf/releases/download/v2.6.1/protobuf-2.6.1.tar.gz
| \  
tar -zxf - -C /opt && \  
cd /opt/protobuf-2.6.1 && \  
./configure && make && make install  
  
RUN \  
wget -O /usr/local/lib/hsdis-amd64.so \  
https://kenai.com/projects/base-hsdis/downloads/download/linux-hsdis-amd64.so  
  
ENV LD_LIBRARY_PATH /usr/local/lib  
  
WORKDIR $DEV_DIR/code/java

