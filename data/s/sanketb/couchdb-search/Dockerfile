# Licensed under the Apache License, Version 2.0 (the "License"); you may not  
# use this file except in compliance with the License. You may obtain a copy
of  
# the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT  
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the  
# License for the specific language governing permissions and limitations
under  
# the License.  
  
FROM debian:jessie  
  
MAINTAINER Sanket Bajoria bajoriasanket@gmail.com  
  
# Set Environment  
ENV JAVA_VERSION_MAJOR=7 \  
JAVA_VERSION_MINOR=80 \  
JAVA_VERSION_BUILD=15 \  
JAVA_PACKAGE=server-jre \  
JAVA_HOME=/jre \  
PATH=${PATH}:/jre/bin \  
MAVEN_VERSION=3.3.3 \  
MAVEN_HOME=/usr/share/maven  
# Add CouchDB user account  
RUN groupadd -r couchdb && useradd -d /usr/src/couchdb -g couchdb couchdb \  
# Get necesary dependencies  
&& apt-get update -y -qq && apt-get install -y --no-install-recommends \  
apt-transport-https \  
build-essential \  
ca-certificates \  
curl \  
erlang-dev \  
erlang-nox \  
erlang-reltool \  
git \  
haproxy \  
supervisor \  
libcurl4-openssl-dev \  
libicu-dev \  
libmozjs185-dev \  
libmozjs185-1.0 \  
openssl \  
python \  
make \  
&& curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
&& apt-get update -y -qq && apt-get install -y nodejs \  
&& npm install -g grunt-cli \  
#Install Java  
&& cd /tmp \  
&& curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie"\  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
| gunzip -c - | tar -xf - \  
&& mv jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR}/jre /jre \  
#Install Maven  
&& curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \  
# Acquire CouchDB source code  
&& cd /usr/src && mkdir couchdb \  
&& git clone -b dreyfus https://github.com/sanketbajoria/couchdb.git \  
&& cd couchdb \  
# Build couchdb  
&& ./configure \--disable-docs \  
&& make \  
# Clone Clouseau  
&& cd /usr/src \  
&& git clone https://github.com/cloudant-labs/clouseau \  
&& cd /usr/src/clouseau \  
&& mvn -Dmaven.test.skip=true install clean\  
&& chmod +x /usr/src/clouseau && chown -R couchdb:couchdb /usr/src/clouseau \  
# Remove packages used only for build CouchDB  
&& apt-get purge -y \  
binutils \  
build-essential \  
cpp \  
erlang-dev \  
git \  
libcurl4-openssl-dev \  
libicu-dev \  
libmozjs185-dev \  
openssl \  
make \  
nodejs \  
perl \  
&& apt-get autoremove -y && apt-get clean \  
&& apt-get install -y libicu52 --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* /usr/lib/node_modules src/**/.git .git
/usr/src/couchdb/src/fauxton \  
&& rm -rf /jre/bin/jjs \  
/jre/bin/keytool \  
/jre/bin/orbd \  
/jre/bin/pack200 \  
/jre/bin/policytool \  
/jre/bin/rmid \  
/jre/bin/rmiregistry \  
/jre/bin/servertool \  
/jre/bin/tnameserv \  
/jre/bin/unpack200 \  
/jre/bin/javaws \  
/jre/lib/plugin.jar \  
/jre/lib/javaws.jar \  
/jre/lib/desktop \  
/jre/lib/deploy* \  
/jre/lib/*javafx* \  
/jre/lib/*jfx* \  
/jre/lib/ext/jfxrt.jar \  
/jre/lib/ext/nashorn.jar \  
/jre/lib/jfr \  
/jre/lib/jfr.jar \  
/jre/lib/amd64/libdecora_sse.so \  
/jre/lib/amd64/libprism_*.so \  
/jre/lib/amd64/libfxplugins.so \  
/jre/lib/amd64/libglass.so \  
/jre/lib/amd64/libgstreamer-lite.so \  
/jre/lib/amd64/libjavafx*.so \  
/jre/lib/amd64/libjfx*.so \  
/jre/lib/oblique-fonts \  
/jre/plugin \  
/tmp/* \  
&& find / -name .git -type d | xargs rm -rf \  
&& find / -name .npm -type d | xargs rm -rf \  
&& find / -name node_modules -type d | xargs rm -rf \  
&& find /usr/src/couchdb -name test -type d | xargs rm -rf \  
# permissions  
&& chmod +x /usr/src/couchdb/dev/run && chown -R couchdb:couchdb
/usr/src/couchdb \  
&& mkdir -p /var/log/supervisor/ \  
&& chmod 755 /var/log/supervisor/  
  
#supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
#USER couchdb  
VOLUME ["/usr/src/couchdb/dev/lib", "/usr/src/couchdb/var/log",
"/usr/src/clouseau/target"]  
EXPOSE 5984 15984 25984 35984 15986 25986 35986  
WORKDIR /usr/src/couchdb  
  
#entrypoint  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
#ENTRYPOINT ["/usr/bin/supervisord"]  
ENTRYPOINT ["/docker-entrypoint.sh"]

