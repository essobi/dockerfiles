FROM ubuntu  
  
#set the environment arguments  
ENV FASTDHT_PATH=/FastDHT \  
FASTDHT_BASE_PATH=/data \  
BERKELEY_DB_VERSION=6.1.26  
#get all the dependences  
RUN apt-get update && apt-get install -y \  
gcc \  
git \  
make \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
#create the dir  
RUN mkdir -p ${FASTDHT_PATH}/fastdht \  
&& mkdir -p ${FASTDHT_BASE_PATH} \  
&& mkdir -p ${FASTDHT_PATH}/libfastcommon \  
&& mkdir -p ${FASTDHT_PATH}/berkeleydb  
  
#compile the libfastcommon  
WORKDIR ${FASTDHT_PATH}/libfastcommon  
  
RUN git clone https://github.com/happyfish100/libfastcommon.git
${FASTDHT_PATH}/libfastcommon \  
&& ./make.sh \  
&& ./make.sh install \  
&& rm -rf ${FASTDHT_PATH}/libfastcommon  
  
#compile the berkeleydb  
WORKDIR ${FASTDHT_PATH}/berkeleydb/db-${BERKELEY_DB_VERSION}/build_unix  
  
RUN wget "http://download.oracle.com/berkeley-
db/db-${BERKELEY_DB_VERSION}.tar.gz" -P ${FASTDHT_PATH}/berkeleydb \  
&& tar zxvf ${FASTDHT_PATH}/berkeleydb/db-${BERKELEY_DB_VERSION}.tar.gz -C
${FASTDHT_PATH}/berkeleydb \  
&& ../dist/configure --prefix=/usr \  
&& make \  
&& make install \  
&& rm -rf ${FASTDHT_PATH}/berkeleydb  
  
#compile the fastdht  
WORKDIR ${FASTDHT_PATH}/fastdht  
  
RUN git clone https://github.com/happyfish100/fastdht.git
${FASTDHT_PATH}/fastdht \  
&& ./make.sh \  
&& ./make.sh install \  
&& rm -rf ${FASTDHT_PATH}/fastdht  
  
EXPOSE 11411  
ADD start.sh /usr/bin/  
  
#make the start.sh executable  
RUN chmod 777 /usr/bin/start.sh  
  
ENTRYPOINT ["/usr/bin/start.sh"]  
  
MAINTAINER LionHeart <LionHeart_fxc@163.com>

