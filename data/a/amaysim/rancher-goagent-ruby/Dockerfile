FROM ruby:2.3.1  
ENV PHANTOMJS_VERSION 2.1.1  
ENV GOCD_VERSION=16.7.0 \  
GOCD_RELEASE=go-agent \  
GOCD_REVISION=3819 \  
GOCD_HOME=/opt/go-agent \  
PATH=$GOCD_HOME:$PATH  
  
ENV
GOCD_REPO=https://download.go.cd/binaries/${GOCD_VERSION}-${GOCD_REVISION}/generic
\  
GOCD_RELEASE_ARCHIVE=${GOCD_RELEASE}-${GOCD_VERSION}-${GOCD_REVISION}.zip \  
SERVER_WORK_DIR=${GOCD_HOME}/work  
  
# Install phantomjs  
RUN cd /tmp && \  
curl -L -O
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 && \  
tar xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \  
mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs /usr/local/bin
&& \  
rm -rf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64  
  
# Install packages  
RUN apt-get update && apt-get install -y --no-install-recommends zip unzip
nodejs  
  
# Install GoCD Agent  
RUN mkdir /var/log/go-agent /var/run/go-agent &&\  
cd /opt && curl -sSL ${GOCD_REPO}/${GOCD_RELEASE_ARCHIVE} -O && unzip
${GOCD_RELEASE_ARCHIVE} && rm ${GOCD_RELEASE_ARCHIVE} &&\  
mv /opt/${GOCD_RELEASE}-${GOCD_VERSION} ${GOCD_HOME} &&\  
chmod 774 ${GOCD_HOME}/*.sh &&\  
mkdir -p ${GOCD_HOME}/work &&\  
gem install bundler  
  
# Install Java  
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
  
ENV LANG C.UTF-8  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/jre  
  
ENV JAVA_VERSION 8u102  
ENV JAVA_DEBIAN_VERSION 8u102-b14.1-1~bpo8+1  
ENV CA_CERTIFICATES_JAVA_VERSION 20140324  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
python-dev \  
openjdk-8-jre-headless="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
# Install AWS CLi  
RUN curl -O https://bootstrap.pypa.io/get-pip.py &&\  
python get-pip.py &&\  
rm get-pip.py &&\  
pip install awscli &&\  
pip install docker-compose  
  
COPY gocd-entrypoint.sh /usr/bin/docker-entrypoint.sh  
RUN chmod +x /usr/bin/docker-entrypoint.sh  
  
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]

