FROM alpine:edge  
  
MAINTAINER Troy Kelly <troy.kelly@really.ai>  
  
ENV VERSION=v9.5.0 NPM_VERSION=5 YARN_VERSION=latest  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Node.JS with PM2 and git" \  
org.label-schema.description="Provides node with working pm2 and git. Supports
starting apps from pm2.json with feedback to keymetrics." \  
org.label-schema.url="https://really.ai/about/opensource" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/reallyreally/docker-node-pm2-git"
\  
org.label-schema.vendor="Really Really, Inc." \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
# For base builds  
#ENV CONFIG_FLAGS="--fully-static --without-npm" DEL_PKGS="libstdc++"
RM_DIRS=/usr/include  
#ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true  
ENV CHROME_BIN=/usr/bin/chromium-browser  
  
RUN echo @edge http://dl-cdn.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories && \  
echo @edge http://dl-cdn.alpinelinux.org/alpine/edge/main >>
/etc/apk/repositories && \  
echo @edge http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories && \  
apk \--no-cache update && apk \--no-cache upgrade && \  
apk add \--no-cache openssh-client git curl make gcc g++ python \  
linux-headers binutils-gold gnupg libstdc++ udev \  
gifsicle pngquant optipng libjpeg-turbo-utils ttf-opensans nss@edge
chromium@edge && \  
gpg \--keyserver ipv4.pool.sks-keyservers.net \--recv-keys \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE && \  
curl -sSLO https://nodejs.org/dist/${VERSION}/node-${VERSION}.tar.xz && \  
curl -sSL https://nodejs.org/dist/${VERSION}/SHASUMS256.txt.asc | gpg \--batch
\--decrypt | \  
grep " node-${VERSION}.tar.xz\$" | sha256sum -c | grep . && \  
tar -xf node-${VERSION}.tar.xz && \  
cd node-${VERSION} && \  
./configure \--prefix=/usr ${CONFIG_FLAGS} && \  
make -j$(getconf _NPROCESSORS_ONLN) && \  
make install && \  
cd / && \  
if [ -z "$CONFIG_FLAGS" ]; then \  
npm install -g npm@${NPM_VERSION} && \  
find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm -rf
&& \  
if [ -n "$YARN_VERSION" ]; then \  
gpg \--keyserver ipv4.pool.sks-keyservers.net \--recv-keys \  
6A010C5166006599AA17F08146C2130DFD2497F5 && \  
curl -sSL -O https://yarnpkg.com/${YARN_VERSION}.tar.gz -O
https://yarnpkg.com/${YARN_VERSION}.tar.gz.asc && \  
gpg \--batch \--verify ${YARN_VERSION}.tar.gz.asc ${YARN_VERSION}.tar.gz && \  
mkdir /usr/local/share/yarn && \  
tar -xf ${YARN_VERSION}.tar.gz -C /usr/local/share/yarn \--strip 1 && \  
ln -s /usr/local/share/yarn/bin/yarn /usr/local/bin/ && \  
ln -s /usr/local/share/yarn/bin/yarnpkg /usr/local/bin/ && \  
rm ${YARN_VERSION}.tar.gz*; \  
fi; \  
fi && \  
apk del curl linux-headers binutils-gold gnupg ${DEL_PKGS} && \  
rm -rf ${RM_DIRS} /node-${VERSION}* /usr/share/man /tmp/* /var/cache/apk/* \  
/root/.npm /root/.node-gyp /root/.gnupg /usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html
/usr/lib/node_modules/npm/scripts && \  
mkdir -p /usr/src && \  
adduser -D pptruser pptruser && addgroup pptruser audio && addgroup pptruser
video && \  
mkdir /home/pptruser/.ssh && \  
mkdir -p /usr/src/app && \  
touch /home/pptruser/.ssh/repo-key && \  
echo "IdentityFile /home/pptruser/.ssh/repo-key" > /home/pptruser/.ssh/config
&& \  
chmod 600 /home/pptruser/.ssh/config && \  
chmod 600 /home/pptruser/.ssh/repo-key && \  
mkdir -p /home/pptruser/Downloads && \  
mkdir -p /node_modules && \  
npm install pm2 -g && \  
pm2 install pm2-auto-pull  
  
COPY known_hosts /home/pptruser/.ssh/known_hosts  
COPY docker-entrypoint.sh /home/pptruser/  
  
RUN chown -R pptruser:pptruser /home/pptruser && \  
chown -R pptruser:pptruser /node_modules && \  
chown -R pptruser:pptruser /usr/src/app && \  
chmod 755 /home/pptruser/docker-entrypoint.sh  
# Run everything after as non-privileged user.  
USER pptruser  
  
ENTRYPOINT ["/home/pptruser/docker-entrypoint.sh"]  
CMD ["google-chrome-unstable"]  

