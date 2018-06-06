FROM buildpack-deps:jessie  
  
# This is a big big ugly Dockerfile. You should really try not to use it as a
"good" reference....  
MAINTAINER Matt Klich <matt@wayin.com>  
  
#  
# Begin Java | https://github.com/docker-
library/openjdk/blob/a0a4970a343a3c021dad760f2281d20f61931e3c/8-jdk/Dockerfile  
#  
# A few problems with compiling Java from source:  
# 1. Oracle. Licensing prevents us from redistributing the official JDK.  
# 2. Compiling OpenJDK also requires the JDK to be installed, and it gets  
# really hairy.  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
unzip \  
xz-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
openjdk-8-jdk \  
ca-certificates-java \  
&& rm -rf /var/lib/apt/lists/* \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
#  
# End Java  
#  
#  
# Begin Maven | https://github.com/carlossg/docker-
maven/blob/40cbcd2edc2719c64062af39baac6ae38d0becf9/jdk-8/Dockerfile  
#  
ENV MAVEN_VERSION 3.3.9  
RUN mkdir -p /usr/share/maven \  
&& curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
VOLUME /root/.m2  
  
#  
# End Maven  
#  
#  
# Begin Node | https://github.com/nodejs/docker-
node/blob/bf93fccf8e127824cd2478f491502c7d3ad0e1aa/4.4/Dockerfile  
#  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 4.4.7  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
#  
# End Node  
#  

