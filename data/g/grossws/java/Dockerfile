FROM grossws/centos:7  
MAINTAINER Konstantin Gribov <grossws@gmail.com>  
  
ARG MAVEN_VERSION=3.5.3  
ARG
MAVEN_TGZ_URL=https://www.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz  
  
RUN gpg --recv-keys $(curl "https://www.apache.org/dist/maven/KEYS" | gpg
--with-fingerprint --with-colons | grep "^fpr" | cut -d: -f10) \  
&& NEAREST_MAVEN_TGZ_URL=$(curl -sSL
http://www.apache.org/dyn/closer.cgi/${MAVEN_TGZ_URL#https://www.apache.org/dist/}\?asjson\=1
\  
| awk '/"path_info": / { pi=$2; }; /"preferred":/ { pref=$2; }; END { print
pref " " pi; };' \  
| sed -r -e 's/^"//; s/",$//; s/" "//') \  
&& echo "Nearest mirror: $NEAREST_MAVEN_TGZ_URL" \  
&& curl -sSL "$NEAREST_MAVEN_TGZ_URL" -o maven.tar.gz \  
&& curl -sSL $MAVEN_TGZ_URL.asc -o maven.tar.gz.asc \  
&& gpg --verify maven.tar.gz.asc maven.tar.gz \  
&& mkdir -p /opt/maven \  
&& tar xvf maven.tar.gz -C /opt/maven --strip-components=1 \  
&& rm -f maven.tar.gz* \  
&& yum -y install java-1.8.0-openjdk-devel tzdata-java which \  
&& yum clean all \  
&& rm -rf /var/cache/yum \  
&& alternatives --install /usr/bin/mvn mvn /opt/maven/bin/mvn 100  

