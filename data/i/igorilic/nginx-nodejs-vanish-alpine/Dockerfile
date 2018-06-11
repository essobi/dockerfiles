FROM nginx:1.13.7-alpine  
MAINTAINER Igor Ilic  
  
# Node install  
# gpg keys listed at https://github.com/nodejs/node#release-team  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 8.9.2  
  
RUN addgroup -g 1000 node \  
&& adduser -u 1000 -G node -s /bin/sh -D node \  
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
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
77984A986EBC2AA786BC0F66B01FBB92821C587A \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& curl -SLO
"https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION.tar.xz\$" SHASUMS256.txt | sha256sum -c - \  
&& tar -xf "node-v$NODE_VERSION.tar.xz" \  
&& cd "node-v$NODE_VERSION" \  
&& ./configure \  
&& make -j$(getconf _NPROCESSORS_ONLN) \  
&& make install \  
&& apk del .build-deps \  
&& cd .. \  
&& rm -Rf "node-v$NODE_VERSION" \  
&& rm "node-v$NODE_VERSION.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
# Yarn install  
ENV YARN_VERSION 1.3.2  
  
RUN apk add --no-cache --virtual .build-deps-yarn curl gnupg tar \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& mkdir -p /opt/yarn \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/yarn --strip-components=1 \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn/bin/yarn /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz \  
&& apk del .build-deps-yarn  
  
# Varnish and chrome headless install  
ENV VARNISH_BACKEND_ADDRESS 127.0.0.1  
ENV VARNISH_MEMORY 100M  
ENV VARNISH_BACKEND_PORT 8080  
  
RUN apk update && \  
apk upgrade && \  
apk add varnish chromium  
  
# Setup chrome  
# flags from https://github.com/GoogleChrome/lighthouse/blob/master/chrome-
launcher/flags.ts  
CMD [ \  
# Disable various background network services, including extension updating,  
# safe browsing service, upgrade detector, translate, UMA  
"--disable-background-networking", \  
# Disable installation of default apps on first run  
"--disable-default-apps", \  
# Disable all chrome extensions entirely  
"--disable-extensions", \  
# Disable the GPU hardware acceleration  
"--disable-gpu", \  
# Disable syncing to a Google account  
"--disable-sync", \  
# Disable built-in Google Translate service  
"--disable-translate", \  
# Run in headless mode  
"--headless", \  
# Hide scrollbars on generated images/PDFs  
"--hide-scrollbars", \  
# Disable reporting to UMA, but allows for collection  
"--metrics-recording-only", \  
# Mute audio  
"--mute-audio", \  
# Skip first run wizards  
"--no-first-run", \  
# Disable fetching safebrowsing lists, likely redundant due to disable-
background-networking  
"--safebrowsing-disable-auto-update", \  
]  
  

