# VERSION 1.2  
FROM python:2-slim  
  
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>  
  
RUN apt-get update \  
&& apt-get install -y \  
bzip2 \  
wget  
  
ENV FOLDER_NAME compilebench  
ENV VERSION 0.6  
WORKDIR /root  
RUN mkdir ${FOLDER_NAME} \  
&& wget
https://oss.oracle.com/~mason/compilebench/${FOLDER_NAME}-${VERSION}.tar.bz2 \  
&& tar -xf ${FOLDER_NAME}-${VERSION}.tar.bz2 -C $FOLDER_NAME \--strip-
components=1 \  
&& rm ${FOLDER_NAME}-${VERSION}.tar.bz2  
  
# Clean Up  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY run.sh .  
ENTRYPOINT ["./run.sh"]  

