FROM ruby:2.3.7-stretch  
LABEL maintainer="kevin.olbrich@mckesson.com"  
  
ENV NODE_VERSION 8.11.2  
ENV YARN_VERSION 1.7.0  
ENV PHANTOMJS_VERSION 2.1.1  
ENV CHEFDK_VERSION 1.6.11  
ENV DOCKERIZE_VERSION v0.6.0  
ENV JAVA_HOME=/jdk1.6.0_45  
ENV PATH="${JAVA_HOME}/bin:${PATH}"  
ENV RUBYGEMS_VERSION 2.7.7  
# Java  
COPY ./src/jdk-6u45-linux-x64.bin ./jdk-6u45-linux-x64.bin  
RUN chmod a+x ./jdk-6u45-linux-x64.bin  
RUN ./jdk-6u45-linux-x64.bin  
RUN rm ./jdk-6u45-linux-x64.bin  
  
# Java test runner  
RUN apt-get update && apt-get install -y ant  
  
# Node, see: https://github.com/nodejs/docker-
node/blob/master/8/stretch/Dockerfile  
RUN groupadd --gid 1000 node \  
&& useradd --uid 1000 --gid node --shell /bin/bash --create-home node  
  
# gpg keys listed at https://github.com/nodejs/node#release-team  
RUN set -ex \  
&& for key in \  
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
done  
  
RUN ARCH= && dpkgArch="$(dpkg --print-architecture)" \  
&& case "${dpkgArch##*-}" in \  
amd64) ARCH='x64';; \  
ppc64el) ARCH='ppc64le';; \  
s390x) ARCH='s390x';; \  
arm64) ARCH='arm64';; \  
armhf) ARCH='armv7l';; \  
i386) ARCH='x86';; \  
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
components=1 --no-same-owner \  
&& rm "node-v$NODE_VERSION-linux-$ARCH.tar.xz" SHASUMS256.txt.asc
SHASUMS256.txt \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs  
  
RUN set -ex \  
&& for key in \  
6A010C5166006599AA17F08146C2130DFD2497F5 \  
; do \  
gpg --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys "$key" || \  
gpg --keyserver hkp://ipv4.pool.sks-keyservers.net --recv-keys "$key" || \  
gpg --keyserver hkp://pgp.mit.edu:80 --recv-keys "$key" ; \  
done \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz" \  
&& curl -fSLO --compressed
"https://yarnpkg.com/downloads/$YARN_VERSION/yarn-v$YARN_VERSION.tar.gz.asc" \  
&& gpg --batch --verify yarn-v$YARN_VERSION.tar.gz.asc
yarn-v$YARN_VERSION.tar.gz \  
&& mkdir -p /opt \  
&& tar -xzf yarn-v$YARN_VERSION.tar.gz -C /opt/ \  
&& ln -s /opt/yarn-v$YARN_VERSION/bin/yarn /usr/local/bin/yarn \  
&& ln -s /opt/yarn-v$YARN_VERSION/bin/yarnpkg /usr/local/bin/yarnpkg \  
&& rm yarn-v$YARN_VERSION.tar.gz.asc yarn-v$YARN_VERSION.tar.gz  
  
# PhantomJS  
RUN curl --output /usr/local/bin/phantomjs https://s3.amazonaws.com/circle-
downloads/phantomjs-$PHANTOMJS_VERSION \  
&& chmod a+x /usr/local/bin/phantomjs  
  
# CodeClimate  
RUN curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-
latest-linux-amd64 > /usr/local/bin/cc-test-reporter \  
&& chmod a+x /usr/local/bin/cc-test-reporter  
  
# ChefDK  
RUN wget
https://packages.chef.io/stable/ubuntu/14.04/chefdk_$CHEFDK_VERSION-1_amd64.deb
\  
&& dpkg -i chefdk_$CHEFDK_VERSION-1_amd64.deb  
  
# Dockerize  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
# Misc.  
RUN apt-get update && apt-get install -y zip unzip jq  
  
RUN gem update --system $RUBYGEMS_VERSION  

