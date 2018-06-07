FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
# JDK version info from.  
# http://www.oracle.com/technetwork/java/javase/downloads/index.html  
# http://download.oracle.com/otn-
pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-x64.tar.gz  
ENV DEBIAN_FRONTEND noninteractive  
ENV VERSION 8  
ENV UPDATE 161  
ENV BUILD 12  
ENV SIG 2f38c3b165be4555a1fa6e98c45e0808  
ENV JAVA_HOME /usr/lib/jvm/java-${VERSION}-oracle  
ENV JRE_HOME ${JAVA_HOME}/jre  
  
RUN apt-get update && apt-get install locales ca-certificates curl unzip
netcat wget git tzdata -y --no-install-recommends && \  
locale-gen en_US.UTF-8 && \  
localedef -i en_US -c -f UTF-8 en_US.UTF-8 && \  
curl --silent --location --retry 3 --cacert
/etc/ssl/certs/GeoTrust_Global_CA.pem \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-
pub/java/jdk/"${VERSION}"u"${UPDATE}"-b"${BUILD}"/"${SIG}"/jdk-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz
\  
| tar xz -C /tmp && \  
mkdir -p /usr/lib/jvm && mv /tmp/jdk1.${VERSION}.0_${UPDATE} "${JAVA_HOME}" &&
\  
apt-get autoclean && apt-get --purge -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN update-alternatives --install "/usr/bin/java" "java"
"${JRE_HOME}/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"${JRE_HOME}/bin/javaws" 1 && \  
update-alternatives --install "/usr/bin/javac" "javac"
"${JAVA_HOME}/bin/javac" 1 && \  
update-alternatives --install "/usr/bin/jps" "jps" "${JAVA_HOME}/bin/jps" 1 &&
\  
update-alternatives --install "/usr/bin/jstack" "jstack"
"${JAVA_HOME}/bin/jstack" 1 && \  
update-alternatives --install "/usr/bin/jmap" "jmap" "${JAVA_HOME}/bin/jmap" 1
&& \  
update-alternatives --set java "${JRE_HOME}/bin/java" && \  
update-alternatives --set javaws "${JRE_HOME}/bin/javaws" && \  
update-alternatives --set javac "${JAVA_HOME}/bin/javac" && \  
update-alternatives --set jps "${JAVA_HOME}/bin/jps" && \  
update-alternatives --set jstack "${JAVA_HOME}/bin/jstack" && \  
update-alternatives --set jmap "${JAVA_HOME}/bin/jmap"  
  
RUN ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \  
echo "Europe/Moscow" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"' > /etc/default/locale && \  
update-locale LANG="en_US.UTF-8" LANGUAGE="en_US" && \  
dpkg-reconfigure --frontend=noninteractive locales  

