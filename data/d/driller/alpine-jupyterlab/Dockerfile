FROM alpine:latest  
  
RUN apk update \  
&& apk add \  
ca-certificates \  
libstdc++ \  
python3 \  
&& apk add --virtual=build_dependencies \  
cmake \  
gcc \  
g++ \  
make \  
musl-dev \  
python3-dev \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& python3 -m pip --no-cache-dir install pip -U \  
&& python3 -m pip --no-cache-dir install \  
jupyter \  
jupyterlab \  
&& jupyter serverextension enable --py jupyterlab --sys-prefix \  
&& apk del --purge -r build_dependencies \  
&& rm -rf /var/cache/apk/* \  
&& mkdir /notebooks  
  
VOLUME /notebooks  
ENTRYPOINT /usr/bin/jupyter lab --no-browser --ip=0.0.0.0 \--notebook-
dir=/notebooks  
EXPOSE 8888  

