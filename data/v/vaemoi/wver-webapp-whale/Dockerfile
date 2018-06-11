FROM alpine:3.4  
ENV NODE_PREFIX ~/.npm-global  
ENV SYSTEM_PKGS bash build-base ca-certificates cmake curl gcc g++ git libgcc
python openssh libstdc++ linux-headers paxctl subversion mercurial shadow tar
wget  
ENV JS_PKGS nodejs  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk update && \  
apk upgrade && \  
apk add $SYSTEM_PKGS && \  
apk add $JS_PKGS && \  
find ${NODE_PREFIX}/lib/node_modules/npm -name test -o -name .bin -type d |
xargs rm -rf && \  
rm -rf /var/cache/apk/*  
  
RUN npm install -g yarn && \  
yarn help  

