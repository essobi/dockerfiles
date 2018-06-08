FROM ubuntu  
  
MAINTAINER noninteractive  
  
RUN apt-get clean && apt-get update && apt-get -y install libc6 libc6-dev make
gcc libevent-dev libpthread-stubs0-dev  
COPY FastDFS_v4.06.tar.gz /tmp/  
RUN cd /tmp && tar zxf FastDFS_v4.06.tar.gz  
RUN cd /tmp/FastDFS && ./make.sh && ./make.sh install  

