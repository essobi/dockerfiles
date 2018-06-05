FROM ubuntu:14.04  
MAINTAINER vilibald (wvi@apiary.io)  
  
ENV REFRESHED_AT 2015-04-23  
WORKDIR /  
  
RUN apt-get update && apt-get install -y build-essential curl git cmake python
&&\  
curl -sL https://deb.nodesource.com/setup | bash - && apt-get install -y
nodejs &&\  
apt-get clean && \  
curl https://s3.amazonaws.com/mozilla-games/emscripten/releases/emsdk-
portable.tar.gz > emsdk-portable.tar.gz && \  
tar xzf emsdk-portable.tar.gz && \  
cd emsdk_portable && \  
./emsdk update && ./emsdk install latest && \  
./emsdk activate latest && \  
find /emsdk_portable -name "*.o" -exec rm {} \; && \  
find /emsdk_portable -name "*.a" -exec rm {} \; && \  
rm -rf /emsdk_portable/clang/fastcomp/src && \  
rm -rf /emsdk_portable/emscripten/master/.git && \  
for prog in em++ em-config emar emcc emconfigure emmake emranlib emrun
emscons; do \  
ln -sf /emsdk_portable/emscripten/master/$prog /usr/local/bin; done \  
&& apt-get -y --purge remove curl git cmake && apt-get -y autoremove && apt-
get clean  
  
VOLUME ["/src"]  
WORKDIR /src  
  

