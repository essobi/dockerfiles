FROM golang:1.5.1  
ENV HEKAD_VERSION v0.10.0b1  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y cmake python-sphinx protobuf-compiler debhelper && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN git clone -b ${HEKAD_VERSION} \--depth 1 https://github.com/mozilla-
services/heka.git /heka  
  
WORKDIR /heka  
RUN /bin/bash -c 'source build.sh'  
  
RUN for i in decoders encoders filters modules; do \  
mkdir -p /usr/share/heka/lua_${i} && \  
cp /heka/sandbox/lua/${i}/* /usr/share/heka/lua_${i}; \  
done && \  
cp /heka/build/heka/lib/luasandbox/modules/* /usr/share/heka/lua_modules  
  
EXPOSE 4881  
WORKDIR /heka/build/heka/bin  
CMD ["/heka/build/heka/bin/hekad", "--config", "/app/config.toml"]  

