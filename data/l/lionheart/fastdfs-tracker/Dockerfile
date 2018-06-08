FROM ubuntu  
  
ENV FASTDFS_PATH=/fastDFS \  
FASTDFS_BASE_PATH=/data  
  
#get all the dependences  
RUN apt-get update && apt-get install -y \  
gcc \  
git \  
make \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
#create the dirs to store the files downloaded from internet  
RUN mkdir -p ${FASTDFS_PATH}/libfastcommon \  
&& mkdir -p ${FASTDFS_PATH}/fastdfs \  
&& mkdir ${FASTDFS_BASE_PATH}  
  
#compile the libfastcommon  
WORKDIR ${FASTDFS_PATH}/libfastcommon  
  
RUN git clone https://github.com/happyfish100/libfastcommon.git
${FASTDFS_PATH}/libfastcommon \  
&& ./make.sh \  
&& ./make.sh install \  
&& rm -rf ${FASTDFS_PATH}/libfastcommon  
  
#compile the fastdfs  
WORKDIR ${FASTDFS_PATH}/fastdfs  
  
RUN git clone https://github.com/happyfish100/fastdfs.git
${FASTDFS_PATH}/fastdfs \  
&& ./make.sh \  
&& ./make.sh install \  
&& rm -rf ${FASTDFS_PATH}/fastdfs  
  
EXPOSE 22122  
ADD start.sh /usr/bin/  
  
#make the start.sh executable  
RUN chmod 777 /usr/bin/start.sh  
  
ENTRYPOINT ["/usr/bin/start.sh"]  
  
MAINTAINER LionHeart <LionHeart_fxc@163.com>

