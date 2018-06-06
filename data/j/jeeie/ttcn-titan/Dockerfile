FROM ubuntu:16.04  
MAINTAINER Jiang Ying <jy0000@gmail.com>  
  
USER root  
  
ENV \  
TITAN_VERSION=6.3.1 \  
TTCN3_DIR=/usr/local/titan \  
LOCAL_SRC=/usr/local/src  
  
ENV \  
PATH=${TTCN3_DIR}/bin:${PATH} \  
LD_LIBRARY_PATH=${TTCN3_DIR}/lib:${LD_LIBRARY_PATH} \  
TTCN3_SRC=${LOCAL_SRC}/titan.core  
  
WORKDIR ${LOCAL_SRC}  
  
RUN \  
apt-get clean && \  
apt-get update && \  
apt-get -y install git && \  
mkdir -p /usr/local/titan && \  
apt-get -y install g++ expect libssl-dev libxml2-dev libncurses5-dev flex
bison make && \  
apt-get -y install xutils-dev && \  
git clone https://github.com/eclipse/titan.core titan.core && \  
cd titan.core && \  
git checkout ${TITAN_VERSION} && \  
cd .. && \  
apt-get -y remove git && \  
apt-get clean  
  
ADD Makefile.personal ${TTCN3_SRC}/  
  
WORKDIR ${TTCN3_SRC}  
  
RUN \  
make && \  
make install && \  
rm -rf ${TTCN3_SRC}  
  
WORKDIR /  
  
CMD echo "***************************************" && \  
echo "** This is a demo built in Titan **" && \  
echo "** 4 pass, 1 inconc, 3 fail expected **" && \  
echo "***************************************" && \  
cd ${TTCN3_DIR}/demo && \  
ttcn3_start MyExample && \  
echo "***************************************" && \  
echo "** end of demo **" && \  
echo "***************************************"  
  

