FROM node:8-alpine  
LABEL maintainer="jst@linux.com"  
  
# add yarn build dependencies  
RUN apk --no-cache add -t yarn-build-deps \  
ca-certificates \  
wget \  
tar  
  
# add sharp build dependencies  
RUN apk --no-cache add -t sharp-build-deps \  
\--repository https://dl-3.alpinelinux.org/alpine/edge/testing/ \  
fftw-dev \  
gcc \  
g++ \  
make \  
vips-dev  
  
# add sharp run dependencies  
RUN apk --no-cache add \  
\--repository https://dl-3.alpinelinux.org/alpine/edge/testing/ \  
libc6-compat \  
vips-tools  
  
# install yarn, remove yarn build dependencies  
RUN cd /usr/local/bin && \  
wget https://yarnpkg.com/latest.tar.gz && \  
tar zvxf latest.tar.gz && \  
ln -s /usr/local/bin/dist/bin/yarn.js /usr/local/bin/yarn.js && \  
apk del yarn-build-deps  
  
WORKDIR /usr/src/app  

