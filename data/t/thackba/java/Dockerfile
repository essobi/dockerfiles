FROM ubuntu:latest  
MAINTAINER mail@thackbarth.net  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY DSTRootCAX3.pem /  
COPY LetsEncryptAuthorityX3.pem /  
  
RUN apt-get update && \  
apt-get install -y apt-utils debconf-utils software-properties-common ca-
certificates python && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
keytool -trustcacerts -keystore
/usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts -storepass changeit
-noprompt -importcert -alias DSTRootCAX3 -file /DSTRootCAX3.pem && \  
keytool -trustcacerts -keystore
/usr/lib/jvm/java-8-oracle/jre/lib/security/cacerts -storepass changeit
-noprompt -importcert -alias LetsEncryptAuthorityX3 -file
/LetsEncryptAuthorityX3.pem && \  
rm /DSTRootCAX3.pem && \  
rm /LetsEncryptAuthorityX3.pem && \  
apt-get clean && \  
rm -R /var/cache/oracle-jdk8-installer && \  
rm -rf /var/lib/apt/* /tmp/* /var/tmp/* /var/cache/apt/*

