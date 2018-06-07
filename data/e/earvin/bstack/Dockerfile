FROM node:4.4  
ENV SCALA_VERSION 2.11.7  
ENV SBT_VERSION 0.13.11  
ENV LANG C.UTF-8  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
unzip \  
xz-utils \  
apt-utils \  
zip \  
git \  
subversion \  
emacs nano \  
curl wget \  
nmap \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo 'deb http://httpredir.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
ENV JAVA_VERSION 8u91  
ENV JAVA_DEBIAN_VERSION 8u91-b14-1~bpo8+1  
# see https://bugs.debian.org/775775  
# and https://github.com/docker-library/java/issues/19#issuecomment-70546872  
ENV CA_CERTIFICATES_JAVA_VERSION 20140324  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \  
ca-certificates-java="$CA_CERTIFICATES_JAVA_VERSION" \  
&& rm -rf /var/lib/apt/lists/* \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# see CA_CERTIFICATES_JAVA_VERSION notes above  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
# Install Scala  
## Piping curl directly in tar  
RUN \  
curl -fsL
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C /root/ && \  
echo >> /root/.bashrc && \  
echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc  
  
# Install sbt  
RUN \  
curl -L -o sbt-$SBT_VERSION.deb
http://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
apt-get update && \  
apt-get install sbt && \  
sbt sbtVersion  
  
RUN apt-get update && apt-get -y install python python-pip ruby-dev ruby
locales  
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8  
RUN gem update --no-ri --no-rdoc  
RUN gem install compass --no-ri --no-rdoc  
RUN gem install --pre sass-css-importer  
ENV LANG en_US.utf8  
RUN npm config set unsafe-perm true  
RUN npm i -g phantomjs@1.9.19  
RUN npm i -g bower  
RUN npm i -g ember-cli@2.4.1  
RUN \  
git clone https://github.com/facebook/watchman.git &&\  
cd watchman &&\  
git checkout v3.5.0 &&\  
./autogen.sh &&\  
./configure &&\  
make &&\  
make install  
  
EXPOSE 4200 35729 9000  
# run ember server on container start  
ENTRYPOINT ["/usr/local/bin/ember"]  
CMD ["server"]  

