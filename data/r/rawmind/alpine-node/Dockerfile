FROM rawmind/alpine-monit:5.25-0  
MAINTAINER Raul Sanchez <rawmind@gmail.com>  
  
# ENV VERSION=v0.10.46 CFLAGS="-D__USE_MISC" NPM_VERSION=2  
# ENV VERSION=v0.12.15 NPM_VERSION=2  
# ENV VERSION=v4.7.3 NPM_VERSION=2  
# ENV VERSION=v5.12.0 NPM_VERSION=3  
# ENV VERSION=v6.9.5 NPM_VERSION=3  
# ENV VERSION=v7.5.0 NPM_VERSION=3  
# ENV VERSION=v8.11.2 NPM_VERSION=5 YARN_VERSION=latest  
# ENV VERSION=v9.11.1 NPM_VERSION=5 YARN_VERSION=latest  
# ENV VERSION=v10.1.0 NPM_VERSION=5 YARN_VERSION=latest  
  
ENV SERVICE_NAME=node \  
SERVICE_HOME=/opt/node \  
SERVICE_VERSION=10.1.0 \  
NPM_VERSION=6  
ENV PATH=${SERVICE_HOME}/bin:${PATH} \  
SERVICE_CONF=${SERVICE_HOME}/etc/haproxy.cfg \  
SERVICE_URL=https://nodejs.org/dist/v${SERVICE_VERSION} \  
SERVICE_RELEASE=node-v${SERVICE_VERSION} \  
CONFIG_FLAGS="" \  
#DEL_PKGS="libgcc libstdc++" \  
RM_DIRS="/opt/src /usr/include"  
  
RUN apk add --no-cache curl make gcc g++ python linux-headers paxctl libgcc
libstdc++ gnupg && \  
for server in ipv4.pool.sks-keyservers.net keyserver.pgp.com ha.pool.sks-
keyservers.net; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A && break;\  
done && \  
mkdir -p /opt/src; cd /opt/src && \  
curl -O -sSL ${SERVICE_URL}/${SERVICE_RELEASE}.tar.gz && \  
curl -O -sSL ${SERVICE_URL}/SHASUMS256.txt.asc && \  
gpg --verify SHASUMS256.txt.asc && \  
grep ${SERVICE_RELEASE}.tar.gz SHASUMS256.txt.asc | sha256sum -c - && \  
tar -zxf ${SERVICE_RELEASE}.tar.gz && \  
cd ${SERVICE_RELEASE} && \  
export GYP_DEFINES="linux_use_gold_flags=0" && \  
./configure --prefix=${SERVICE_HOME} ${CONFIG_FLAGS} && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
make -j${NPROC} -C out mksnapshot BUILDTYPE=Release && \  
paxctl -cm out/Release/mksnapshot && \  
make -j${NPROC} && \  
make install && \  
paxctl -cm ${SERVICE_HOME}/bin/node && \  
cd / && \  
if [ -x ${SERVICE_HOME}/bin/npm ]; then \  
npm install -g npm@${NPM_VERSION} && \  
find ${SERVICE_HOME}/lib/node_modules/npm -name test -o -name .bin -type d |
xargs rm -rf; \  
fi && \  
apk del make gcc g++ python linux-headers paxctl gnupg ${DEL_PKGS} && \  
rm -rf /etc/ssl \  
${RM_DIRS} \  
/usr/share/man \  
/tmp/* \  
/var/cache/apk/* \  
/root/.npm \  
/root/.node-gyp \  
/root/.gnupg \  
${SERVICE_HOME}/lib/node_modules/npm/man \  
${SERVICE_HOME}/lib/node_modules/npm/doc \  
${SERVICE_HOME}/lib/node_modules/npm/html  

