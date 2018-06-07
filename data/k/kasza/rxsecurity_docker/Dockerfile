FROM ruby:2.3.3  
#FROM heroku/heroku:16  
MAINTAINER Colibri Software <support@colibri-software.com>  
  
ENV FREETDS_VERSION freetds-1.00.49  
ENV TDSVER 7.3  
# Allow secure transport  
RUN apt-get update && apt-get install -y apt-transport-https  
  
# Add Heroku repository and key  
RUN echo "deb https://cli-assets.heroku.com/branches/stable/apt ./" > \  
/etc/apt/sources.list.d/heroku.list  
RUN wget -qO- https://cli-assets.heroku.com/apt/release.key | apt-key add -  
  
# Install Heroku CLI, MySQL client, and FreeTDS dependencies  
RUN apt-get update \  
&& apt-get install -y \  
build-essential \  
heroku \  
libc6-dev \  
mysql-client-5.5 \  
#mysql-client-5.7 \  
#mysql-client-core-5.7  
&& rm -rf /var/lib/apt/lists/*  
  
# Install FreeTDS  
RUN curl -s ftp://ftp.freetds.org/pub/freetds/stable/$FREETDS_VERSION.tar.gz \  
| tar xz -C /tmp  
WORKDIR /tmp/$FREETDS_VERSION  
RUN ./configure --with-tdsver=$TDSVER \--enable-msdblib  
RUN make  
RUN make install  
WORKDIR /  
RUN rm -rf /tmp/$FREETDS_VERSION  
  
# Install tiny_tds gem, so review app doesn't have to  
RUN gem install tiny_tds  
  
# Install Node  
# gpg keys listed at https://github.com/nodejs/node#release-team  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
56730D5401028683275BD23C23EFEFE93C4CFFFE \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 8.7.0  
RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \  
&& case "${dpkgArch##*-}" in \  
amd64) ARCH='x64';; \  
ppc64el) ARCH='ppc64le';; \  
s390x) ARCH='s390x';; \  
arm64) ARCH='arm64';; \  
armhf) ARCH='armv7l';; \  
*) echo "unsupported architecture"; exit 1 ;; \  
esac \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-$ARCH.tar.xz" \  
&& curl -SLO --compressed
"https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-$ARCH.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-$ARCH.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
ENV YARN_VERSION 1.2.0  
RUN set -ex \  
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
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  

