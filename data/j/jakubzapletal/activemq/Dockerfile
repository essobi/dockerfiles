FROM jakubzapletal/ubuntu:14.04  
  
MAINTAINER Jakub Zapletal <zapletal.jakub@gmail.com>  
  
RUN \  
rm /etc/apt/sources.list && \  
echo deb http://archive.ubuntu.com/ubuntu trusty main universe multiverse >
/etc/apt/sources.list && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys EEA14886 && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
update-java-alternatives -s java-8-oracle && \  
apt-get install -y oracle-java8-set-default && \  
curl http://archive.apache.org/dist/activemq/apache-activemq/5.9.0/apache-
activemq-5.9.0-bin.tar.gz | tar -xz && \  
mv apache-activemq-5.9.0/conf/activemq.xml apache-
activemq-5.9.0/conf/activemq.xml.orig && \  
awk '/.*stomp.*/{print " <transportConnector name=\"stompssl\"
uri=\"stomp+nio+ssl://0.0.0.0:61612?transport.enabledCipherSuites=SSL_RSA_WITH_RC4_128_SHA,SSL_DH_anon_WITH_3DES_EDE_CBC_SHA\"
/>"}1' apache-activemq-5.9.0/conf/activemq.xml.orig >> apache-
activemq-5.9.0/conf/activemq.xml  
  
EXPOSE 61612 61613 61616 8161  
  
CMD java -Xms1G -Xmx1G -Djava.util.logging.config.file=logging.properties
-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote
-Djava.io.tmpdir=apache-activemq-5.9.0/tmp -Dactivemq.classpath=apache-
activemq-5.9.0/conf -Dactivemq.home=apache-activemq-5.9.0
-Dactivemq.base=apache-activemq-5.9.0 -Dactivemq.conf=apache-
activemq-5.9.0/conf -Dactivemq.data=/data -jar apache-
activemq-5.9.0/bin/activemq.jar start

