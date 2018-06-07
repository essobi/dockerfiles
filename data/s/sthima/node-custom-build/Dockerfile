FROM alpine:3.7  
#  
ENV GIT_NODE_REPO https://github.com/mmarchini/node  
ENV NODE_BRANCH v6.12.3-perf-basic-prof-toggling  
  
RUN apk add --no-cache libstdc++ \  
&& apk add --no-cache --virtual .build-deps \  
binutils-gold \  
curl \  
g++ \  
gcc \  
gnupg \  
libgcc \  
linux-headers \  
make \  
python \  
git \  
&& git clone \--depth 1 $GIT_NODE_REPO -b $NODE_BRANCH /opt/node \  
&& cd /opt/node \  
&& ./configure && make -j$(getconf _NPROCESSORS_ONLN) && make install \  
&& apk del .build-deps \  
&& cd / \  
&& rm -Rf /opt/node  
CMD ["node"]  

