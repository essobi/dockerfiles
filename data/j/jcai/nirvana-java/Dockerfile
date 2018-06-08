FROM debian:wheezy  
MAINTAINER Jun Tsai "jcai@ganshane.com"  
RUN { \  
apt-get update \  
&& apt-get -y install wget \  
&& wget --progress=bar --no-check-certificate -O /tmp/server-
jre-7u79-linux-x64.tar.gz --header "Cookie: oraclelicense=a"
http://download.oracle.com/otn-pub/java/jdk/7u79-b15/server-
jre-7u79-linux-x64.tar.gz \  
&& echo "beb8f9ddab6b3fd9fee7a8ce7652c815 /tmp/server-
jre-7u79-linux-x64.tar.gz" | md5sum -c > /dev/null 2>&1 || echo "ERROR: MD5SUM
MISMATCH" \  
&& tar xzf /tmp/server-jre-7u79-linux-x64.tar.gz \  
&& mkdir -p /usr/lib/jvm/java-7-oracle \  
&& mv jdk1.7.0_79/* /usr/lib/jvm/java-7-oracle/ \  
&& rm -rf jdk1.7.0_79 && rm /tmp/server-jre-7u79-linux-x64.tar.gz \  
&& apt-get -y purge wget && apt-get -y autoremove&& apt-get clean \  
&& chown root:root -R /usr/lib/jvm/java-7-oracle \  
&& ln -s /usr/lib/jvm/java-7-oracle/bin/* /usr/local/bin/ ;\  
}  
ENV JAVA_HOME=/usr/lib/jvm/java-7-oracle  
  

