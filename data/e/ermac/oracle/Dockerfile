# Dockerizing a base images with:  
#  
# - Debian Stretch  
# - Oracle JDK 8u121  
#  
# Build: docker build -t ermac/oracle:jdk8u131 .  
#  
# Run: docker run -ti ermac/oracle:jdk8u131 bash  
#  
# Example: docker run -it --rm ermac/oracle:jdk8u131 java -version  
#  
FROM debian:stretch  
  
MAINTAINER Fabio Martino <fabiomartino@libero.it>  
  
ENV JAVA_VERSION=8u131 \  
JAVA_HOME=/usr/lib/jvm \  
PATH=${PATH}:/usr/lib/jvm/bin \  
LANG=C.UTF-8  
# JRE_HOME=${JAVA_HOME}/jre \  
# JVM_OPTS="" \  
# JAVA_VERSION_URL_TOKEN d54c1d3a095b4ff2b6607d096fa80163  
# JDK_MD5SUM 75b2cb2249710d822a60f83e28860053  
# JCE_MD5SUM b3c7031bc65c28c2340302065e7d00d3  
RUN (apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install wget
unzip)  
  
RUN (wget --progress=bar:force --no-check-certificate -O
/tmp/jdk-8u131-linux-x64.tar.gz --header "Cookie: oraclelicense=a"
http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz
&&\  
echo "75b2cb2249710d822a60f83e28860053 /tmp/jdk-8u131-linux-x64.tar.gz" |
md5sum -c > /dev/null 2>&1 || (echo "ERROR: MD5SUM MISMATCH"; exit 1) &&\  
tar xzf /tmp/jdk-8u131-linux-x64.tar.gz &&\  
mv jdk1.8.0_131 ${JAVA_HOME} &&\  
rm -rf jdk1.8.0_131 && rm /tmp/jdk-8u131-linux-x64.tar.gz &&\  
chown root:root -R ${JAVA_HOME} &&\  
wget --progress=bar:force --no-check-certificate -O /tmp/jce_policy-8.zip
--header "Cookie: oraclelicense=a" http://download.oracle.com/otn-
pub/java/jce/8/jce_policy-8.zip &&\  
echo "b3c7031bc65c28c2340302065e7d00d3 /tmp/jce_policy-8.zip" | md5sum -c >
/dev/null 2>&1 || (echo "ERROR: MD5SUM MISMATCH"; exit 1) &&\  
unzip -jo -d ${JAVA_HOME}/jre/lib/security /tmp/jce_policy-8.zip &&\  
rm -rf ${JAVA_HOME}/*src.zip \  
${JAVA_HOME}/THIRDPARTYLICENSEREADME*.txt \  
${JAVA_HOME}/COPYRIGHT \  
${JAVA_HOME}/LICENSE \  
${JAVA_HOME}/README.html \  
/var/lib/apt/lists/* \  
/var/cache/apt/* \  
/tmp/* \  
/var/tmp/*)  
  
RUN (update-alternatives --install /usr/bin/java java ${JAVA_HOME}/bin/java 1
&&\  
update-alternatives --set java ${JAVA_HOME}/bin/java &&\  
update-alternatives --install /usr/bin/javac javac ${JAVA_HOME}/bin/javac 1
&&\  
update-alternatives --set javac ${JAVA_HOME}/bin/javac &&\  
update-alternatives --install /usr/bin/javaws javaws ${JAVA_HOME}/bin/javaws 1
&&\  
update-alternatives --set javaws ${JAVA_HOME}/bin/javaws)  

