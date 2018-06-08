FROM openjdk:8u111-jdk-alpine  
  
ENV VERSION=v7.2.1 NPM_VERSION=3  
  
ENV CONFIG_FLAGS="--fully-static --without-npm" DEL_PKGS="libstdc++"
RM_DIRS=/usr/include  
  
ENV PATH ${PATH}:/root/.yarn/bin  
  
RUN apk add --no-cache curl make gcc g++ python linux-headers paxctl libgcc
libstdc++ gnupg wget tar bash binutils && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 && \  
curl -o node-${VERSION}.tar.gz -sSL
https://nodejs.org/dist/${VERSION}/node-${VERSION}.tar.gz && \  
curl -o SHASUMS256.txt.asc -sSL
https://nodejs.org/dist/${VERSION}/SHASUMS256.txt.asc && \  
gpg --verify SHASUMS256.txt.asc && \  
grep node-${VERSION}.tar.gz SHASUMS256.txt.asc | sha256sum -c - && \  
tar -zxf node-${VERSION}.tar.gz && \  
cd node-${VERSION} && \  
export GYP_DEFINES="linux_use_gold_flags=0" && \  
./configure --prefix=/usr ${CONFIG_FLAGS} && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
make -j${NPROC} -C out mksnapshot BUILDTYPE=Release && \  
paxctl -cm out/Release/mksnapshot && \  
make -j${NPROC} && \  
make install && \  
paxctl -cm /usr/bin/node && \  
/bin/bash && \  
touch ~/.bashrc && \  
curl -o- -L https://yarnpkg.com/install.sh | bash && \  
cd / && \  
apk del curl make gcc g++ python linux-headers paxctl gnupg wget tar bash
${DEL_PKGS} && \  
rm -rf /etc/ssl /node-${VERSION}.tar.gz /SHASUMS256.txt.asc /node-${VERSION}
${RM_DIRS} \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp /root/.gnupg
\  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  

