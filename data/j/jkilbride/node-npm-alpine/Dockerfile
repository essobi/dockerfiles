FROM alpine:3.6  
  
ENV NODE_VERSION=v4.8.6 NPM_VERSION=2  
#ENV NODE_VERSION=v6.12.0 NPM_VERSION=3  
#ENV NODE_VERSION=v8.9.1 NPM_VERSION=5  
#ENV NODE_VERSION=v9.1.0 NPM_VERSION=5  
  
ENV YARN_VERSION=1.3.2  
  
RUN apk upgrade --update \  
&& apk add --no-cache \  
libstdc++ \  
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
&& for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& mkdir -p /usr/local/src \  
&& cd /usr/local/src \  
&& curl -SLO
"https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/${NODE_VERSION}/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-${NODE_VERSION}.tar.xz\$" SHASUMS256.txt | sha256sum -c - \  
&& tar -xf "node-${NODE_VERSION}.tar.xz" \  
&& cd "node-${NODE_VERSION}" \  
&& ./configure --prefix=/usr \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& if [ -x /usr/bin/npm ]; then \  
npm install -g npm@${NPM_VERSION} && \  
find /usr/lib/node_modules/npm -name test -o -name .bin -type d | xargs rm
-rf; \  
fi \  
&& cd /usr/local/src \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& curl -fSLO
"https://yarnpkg.com/downloads/${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz.asc"
\  
&& gpg --batch --verify yarn-v${YARN_VERSION}.tar.gz.asc
yarn-v${YARN_VERSION}.tar.gz \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v${YARN_VERSION}.tar.gz -C /opt/yarn --strip 1 \  
&& ln -s /opt/yarn/bin/yarn /usr/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/bin/yarnpkg \  
&& apk del .build-deps \  
&& rm -rf /usr/local/src /tmp/* /usr/share/man /var/cache/apk/* \  
/root/.npm /root/.node-gyp /root/.gnupg /usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc /usr/lib/node_modules/npm/html /etc/ssl \  
/usr/include/node \  
&& mv -f /etc/profile.d/color_prompt /etc/profile.d/color_prompt.sh  
  
COPY aliases.sh /etc/profile.d/  
  
LABEL maintainer="Jeff Kilbride <jeff@kilbride.com>" \  
org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.name="Node / NPM Alpine" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/jeff-kilbride/node-npm-alpine"

