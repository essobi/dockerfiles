FROM ubuntu:xenial  
  
MAINTAINER Dmitrii Zolotov <dzolotov@herzen.spb.ru>  
  
ENV JAVA_HOME /jdk  
ENV JRE_HOME $JAVA_HOME/jre  
ENV JDK_HOME /jdk  
ENV PATH $PATH:$JAVA_HOME/bin:/jdk/bin  
ENV DEBIAN_FRONTEND noninteractive  
ENV JAVA_VERSION 9  
ENV JCE_VERSION 9  
ENV JAVA_BUILD 181  
  
RUN apt-get update && apt-get install -y curl unzip && \  
(curl -L -k -b "oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}+${JAVA_BUILD}/jdk-${JAVA_VERSION}_linux-x64_bin.tar.gz
| gunzip -c | tar x) \  
&& mv /jdk-${JAVA_VERSION} /jdk && cd /tmp && \  
curl -O https://letsencrypt.org/certs/isrgrootx1.der && \  
curl -O https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.der && \  
curl -O https://letsencrypt.org/certs/lets-encrypt-x4-cross-signed.der && \  
curl -O https://letsencrypt.org/certs/lets-encrypt-x1-cross-signed.der && \  
curl -O https://letsencrypt.org/certs/letsencryptauthorityx1.der && \  
curl -O https://letsencrypt.org/certs/lets-encrypt-x2-cross-signed.der && \  
curl -O https://letsencrypt.org/certs/letsencryptauthorityx2.der && \  
keytool -importcert -alias isrgrootx1 -keystore /jdk/lib/security/cacerts
-storepass changeit -noprompt -file /tmp/isrgrootx1.der && \  
keytool -importcert -alias letsencryptauthorityx1 -keystore
/jdk/lib/security/cacerts -storepass changeit -noprompt -file
/tmp/letsencryptauthorityx1.der && \  
keytool -importcert -alias letsencryptauthorityx2 -keystore
/jdk/lib/security/cacerts -storepass changeit -noprompt -file
/tmp/letsencryptauthorityx2.der && \  
keytool -importcert -alias lets-encrypt-x1-cross-signed -keystore
/jdk/lib/security/cacerts -storepass changeit -noprompt -file /tmp/lets-
encrypt-x1-cross-signed.der && \  
keytool -importcert -alias lets-encrypt-x2-cross-signed -keystore
/jdk/lib/security/cacerts -storepass changeit -noprompt -file /tmp/lets-
encrypt-x2-cross-signed.der && \  
keytool -importcert -alias lets-encrypt-x3-cross-signed -keystore
/jdk/lib/security/cacerts -storepass changeit -noprompt -file /tmp/lets-
encrypt-x3-cross-signed.der && \  
keytool -importcert -alias lets-encrypt-x4-cross-signed -keystore
/jdk/lib/security/cacerts -storepass changeit -noprompt -file /tmp/lets-
encrypt-x4-cross-signed.der && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  

