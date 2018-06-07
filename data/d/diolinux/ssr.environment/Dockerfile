FROM library/alpine:3.7  
LABEL maintainer="Gerardo Junior <me@gerardo-junior.com>"  
  
ARG NODE_VERSION=8.11.1  
ARG YARN_VERSION=1.5.1  
ENV COMPILE_DEPS .build-deps \  
binutils-gold \  
curl \  
g++ \  
gcc \  
gnupg \  
libgcc \  
linux-headers \  
make \  
python \  
tar \  
xz  
  
# Install compile app dependencies  
RUN apk add --no-cache --virtual ${COMPILE_DEPS}  
  
# Install run app dependencies  
RUN apk --update add --virtual .persistent-deps \  
sudo \  
libstdc++  
  
RUN cd /tmp  
  
# Create project directory  
RUN mkdir -p /usr/share/src  
  
# Create user node  
RUN set -xe && \  
addgroup -g 1000 node && \  
adduser -u 1000 -G node -s /bin/sh -D node && \  
echo "node ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers.d/default && \  
chown -Rf node /usr/share/src  
  
# Compile and install node  
ENV NODE_SOURCE_URL https://nodejs.org/dist  
RUN for key in \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
; do \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \  
done && \  
curl -SLO "${NODE_SOURCE_URL}/v${NODE_VERSION}/node-v${NODE_VERSION}.tar.xz"
&& \  
curl -SLO --compressed
"${NODE_SOURCE_URL}/v${NODE_VERSION}/SHASUMS256.txt.asc" && \  
gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc && \  
grep " node-v${NODE_VERSION}.tar.xz\$" SHASUMS256.txt | sha256sum -c - && \  
tar -Jxf "node-v${NODE_VERSION}.tar.xz" && \  
cd "node-v${NODE_VERSION}" && \  
sh ./configure && \  
make -j$(getconf _NPROCESSORS_ONLN) && \  
make install && \  
cd .. && \  
npm i npm@latest -g && \  
unset NODE_SOURCE_URL  
  
# Compile and install yarn  
ENV YARN_SOURCE_URL https://yarnpkg.com/downloads  
RUN for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \  
done && \  
curl -fSLO --compressed
"${YARN_SOURCE_URL}/${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz" && \  
curl -fSLO --compressed
"${YARN_SOURCE_URL}/${YARN_VERSION}/yarn-v${YARN_VERSION}.tar.gz.asc" && \  
gpg --batch --verify yarn-v${YARN_VERSION}.tar.gz.asc
yarn-v${YARN_VERSION}.tar.gz && \  
mkdir -p /opt && \  
tar -xzf yarn-v${YARN_VERSION}.tar.gz -C /opt/ && \  
ln -s /opt/yarn-v${YARN_VERSION}/bin/yarn /usr/local/bin/yarn && \  
ln -s /opt/yarn-v${YARN_VERSION}/bin/yarnpkg /usr/local/bin/yarnpkg && \  
unset YARN_SOURCE_URL  
  
# Cleanup system  
RUN apk del ${COMPILE_DEPS} && \  
rm -Rf /var/cache/apk/* /tmp/* $HOME/* && \  
unset NODE_VERSION \  
YARN_VERSION  
  
# Variables of nuxt configure  
ENV HOST 0.0.0.0  
# Copy scripts  
COPY ./tools/entrypoint.sh /usr/local/bin/entrypoint.sh  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
# Set project directory  
VOLUME ["/usr/share/src"]  
WORKDIR /usr/share/src  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  
USER node  
EXPOSE 3000

