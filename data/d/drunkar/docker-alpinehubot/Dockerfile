FROM alpine:3.4  
MAINTAINER Drunkar <drunkars.p@gmail.com>  
  
##############################################################################  
# timezone: tokyo  
##############################################################################  
RUN apk --update add tzdata && \  
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
apk del tzdata && \  
rm -rf /var/cache/apk/*  
  
##############################################################################  
# node.js  
##############################################################################  
ENV VERSION=v6.3.1 NPM_VERSION=3  
  
# For base builds  
# ENV CONFIG_FLAGS="--without-npm" RM_DIRS=/usr/include  
# ENV CONFIG_FLAGS="--fully-static --without-npm" DEL_PKGS="libgcc libstdc++"
RM_DIRS=/usr/include  
  
RUN apk update && apk add --no-cache curl make gcc g++ python linux-headers
paxctl libgcc libstdc++ gnupg && \  
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
cd / && \  
if [ -x /usr/bin/npm ]; then \  
npm install -g npm@${NPM_VERSION} && \  
find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm
-rf; \  
fi && \  
apk del curl make gcc g++ python linux-headers paxctl gnupg ${DEL_PKGS} && \  
rm -rf /etc/ssl /node-${VERSION}.tar.gz /SHASUMS256.txt.asc /node-${VERSION}
${RM_DIRS} \  
/usr/share/man /tmp/* /var/cache/apk/* /root/.npm /root/.node-gyp /root/.gnupg
\  
/usr/lib/node_modules/npm/man /usr/lib/node_modules/npm/doc
/usr/lib/node_modules/npm/html  
  
##############################################################################  
# hubot  
##############################################################################  
ENV HUBOT_HOME /opt/hubot  
  
RUN apk update && apk add \  
bash \  
supervisor \  
redis \  
build-base \  
gcc \  
g++ \  
gcc-objc \  
libtool \  
libc6-compat \  
make \  
expat \  
expat-dev \  
python \  
wget \  
gnupg \  
tar \  
git \  
zip \  
curl \  
wget \  
&& rm -rf /var/cache/apk/*  
  
# Copy system files into place  
COPY systemconfig.sh /tmp/systemconfig.sh  
COPY redis.conf $HUBOT_HOME/redis/redis.conf  
  
RUN mkdir -p /opt/hubot  
RUN addgroup hubot && \  
adduser -h $HUBOT_HOME -D -s /bin/bash -G hubot hubot  
COPY hubot.conf $HUBOT_HOME/config/hubot.conf  
  
# Copy prod mode items into place  
COPY supervisord.conf $HUBOT_HOME/prod/supervisord.ini  
COPY prodmode.sh $HUBOT_HOME/prod/prodmode.sh  
  
# Copy dev mode items into place  
COPY supervisord.dev.conf $HUBOT_HOME/dev/supervisord.ini  
COPY devmode.sh $HUBOT_HOME/dev/devmode.sh  
  
# Setup directories and permissions  
RUN bash -c /tmp/systemconfig.sh  
  
# Install hubot via yo  
WORKDIR $HUBOT_HOME  
RUN npm install --global coffee-script yo generator-hubot node-inspector  
  
USER hubot  
# install hubot  
RUN yo hubot --owner="Drunkar <drunkars.p@gmail.com>" --name="Hubot"
--description="Awesome bot." --adapter=slack --defaults  
  
# Utilize external-scripts-for-npm.json to control which scripts are
installed. As it's already the gatekeeper might as well install from it.  
COPY external-scripts-for-npm.json $HUBOT_HOME/external-scripts-for-npm.json  
# Script to parse external-scripts-for-npm.json to perform the npm install
$script --save  
COPY script-install.py $HUBOT_HOME/script-install.py  
RUN python script-install.py  
  
# Install any dependencies missed by the hubot generate  
RUN npm install  
  
# Expose volumes for long term data storage  
VOLUME /var/lib/redis  
VOLUME $HUBOT_HOME/scripts  
VOLUME $HUBOT_HOME/config  
  
# Exposing node-inspector  
EXPOSE 8123  
EXPOSE 5858  
  
USER root  
ENV PATH
/opt/hubot/node_modules/.bin:/opt/hubot/node_modules/hubot/node_modules/.bin:${PATH}  
CMD /usr/bin/prodmode  

