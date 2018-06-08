FROM krallin/ubuntu-tini:14.04  
  
ENV VERSION 8  
ENV UPDATE 131  
ENV BUILD 11  
#Oracle introduced (around 1.8u131) a hash in the link to download java for
some reason.  
#It seems to be static for a version. Go to download site and check current
one if you have problems.  
ENV HASH d54c1d3a095b4ff2b6607d096fa80163  
  
ENV JAVA_HOME /usr/lib/jvm/java-${VERSION}-oracle  
ENV JRE_HOME ${JAVA_HOME}/jre  
  
RUN apt-get update && apt-get install ca-certificates curl \  
gcc libc6-dev libssl-dev make \  
-y \--no-install-recommends && \  
curl \--silent \--location \--retry 3 \--cacert
/etc/ssl/certs/GeoTrust_Global_CA.pem \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-
pub/java/jdk/"${VERSION}"u"${UPDATE}"-b"${BUILD}"/"${HASH}"/jdk-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz
\  
| tar xz -C /tmp && \  
mkdir -p /usr/lib/jvm && mv /tmp/jdk1.${VERSION}.0_${UPDATE} "${JAVA_HOME}" &&
\  
curl \--silent \--location \--retry 3 \--cacert
/etc/ssl/certs/GlobalSign_Root_CA.pem \  
https://www.openssl.org/source/openssl-1.0.2e.tar.gz \  
| tar xz -C /tmp && \  
cd /tmp/openssl-1.0.2e && \  
./config \--prefix=/usr && \  
make clean && make && make install && \  
apt-get remove \--purge \--auto-remove -y \  
gcc \  
libc6-dev \  
libssl-dev \  
make && \  
apt-get autoclean && apt-get \--purge -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
update-alternatives \--install "/usr/bin/java" "java" "${JRE_HOME}/bin/java" 1
&& \  
update-alternatives \--install "/usr/bin/javac" "javac"
"${JAVA_HOME}/bin/javac" 1 && \  
update-alternatives \--set java "${JRE_HOME}/bin/java" && \  
update-alternatives \--set javac "${JAVA_HOME}/bin/javac"  
  
CMD ["sh", "-c", "${JAVA_HOME}/bin/jjs"]

