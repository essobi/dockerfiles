FROM ubuntu:14.04  
  
MAINTAINER Jason Pell  
  
RUN apt-get -y install wget  
  
RUN wget --progress=bar --no-check-certificate -O /tmp/server-
jre-7u51-linux-x64.tar.gz --header "Cookie: oraclelicense=a"
http://download.oracle.com/otn-pub/java/jdk/7u51-b13/server-
jre-7u51-linux-x64.tar.gz  
  
# Check the checksum, if it fails, print an error message  
RUN echo "c5a034f4222bac326101799bcb20509c /tmp/server-
jre-7u51-linux-x64.tar.gz" | md5sum -c > /dev/null 2>&1 || echo "ERROR: MD5SUM
MISMATCH"  
  
RUN tar xzf /tmp/server-jre-7u51-linux-x64.tar.gz  
RUN mkdir -p /usr/lib/jvm/java-7-oracle  
RUN mv jdk1.7.0_51/jre /usr/lib/jvm/java-7-oracle/jre  
RUN rm -rf jdk1.7.0_51 && rm /tmp/server-jre-7u51-linux-x64.tar.gz  
RUN chown root:root -R /usr/lib/jvm/java-7-oracle  
RUN update-alternatives --install /usr/bin/java java
/usr/lib/jvm/java-7-oracle/jre/bin/java 1  
RUN update-alternatives --set java /usr/lib/jvm/java-7-oracle/jre/bin/java  

