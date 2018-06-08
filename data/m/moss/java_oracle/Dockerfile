FROM debian:8  
MAINTAINER Thiago Almeida <thiagoalmeidasa@gmail.com>  
  
# Specify the Java version. Change to update the JDK.  
ENV VERSION 8  
ENV UPDATE 111  
ENV BUILD 14  
# Update PATH.  
ENV JAVA_HOME /usr/lib/jvm/java-${VERSION}-oracle  
  
# Download and install Oracle Java.  
RUN dpkg --add-architecture i386 && \  
apt-get update && apt-get install ca-certificates curl libncurses5:i386
libstdc++6:i386 zlib1g:i386 git-core -y --no-install-recommends && \  
curl --silent --location --retry 3 --cacert
/etc/ssl/certs/GeoTrust_Global_CA.pem \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-
pub/java/jdk/"${VERSION}"u"${UPDATE}"-b"${BUILD}"/jdk-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz
\  
| tar xz -C /tmp && \  
mkdir -p /usr/lib/jvm && mv /tmp/jdk1.${VERSION}.0_${UPDATE} "${JAVA_HOME}" &&
\  
# Cleaning stuff  
apt-get autoclean && apt-get --purge -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN update-alternatives --install "/usr/bin/java" "java"
"${JAVA_HOME}/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"${JAVA_HOME}/bin/javaws" 1 && \  
update-alternatives --install "/usr/bin/javac" "javac"
"${JAVA_HOME}/bin/javac" 1 && \  
update-alternatives --set java "${JAVA_HOME}/bin/java" && \  
update-alternatives --set javaws "${JAVA_HOME}/bin/javaws" && \  
update-alternatives --set javac "${JAVA_HOME}/bin/javac"  

