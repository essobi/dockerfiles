FROM alpine  
  
RUN apk add \--update \--no-cache \--virtual=.liblinear-deps \  
libgcc \  
libstdc++ \  
libgomp \  
libatomic \  
&& apk add \--update \--no-cache \--virtual=.liblinear-build-deps \  
make \  
g++ \  
gcc \  
git \  
&& mkdir -p /usr/local/src \  
&& cd /usr/local/src \  
&& git clone https://github.com/cjlin1/liblinear.git \  
&& cd liblinear \  
&& make all \  
&& ln -s /usr/local/src/liblinear/train /usr/local/bin/train \  
&& ln -s /usr/local/src/liblinear/predict /usr/local/bin/predict \  
&& apk del .liblinear-build-deps  
  
WORKDIR /data  
  
VOLUME /data  

