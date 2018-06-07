FROM alpine  
RUN apk update \  
&& apk add \--no-cache build-base cmake g++ linux-headers openssl python3-dev
ca-certificates wget vim \  
&& update-ca-certificates  
  
WORKDIR /tmp  
  
ENV HTTP=https://software.ecmwf.int/wiki/download/attachments/45757960 \  
ECCODES=eccodes-2.5.0-Source  
RUN cd /tmp && wget \--output-document=${ECCODES}.tar.gz
${HTTP}/${ECCODES}.tar.gz?api=v2  
RUN tar -zxvf ${ECCODES}.tar.gz  
  
RUN apk add gfortran perl  
RUN cd ${ECCODES} && mkdir build && cd build && cmake .. && make -j2 && make
install  
  
  

