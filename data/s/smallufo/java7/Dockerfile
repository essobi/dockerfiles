FROM smallufo/centos  
MAINTAINER smallufo smallufo@gmail.com  
  
RUN yum -y install java-1.7.0-openjdk java-1.7.0-openjdk-devel  
  
ENV JAVA_HOME /usr/lib/jvm/java  
  
RUN yum clean all;  
  
# WORKDIR /usr/local  
# RUN wget
http://ftp.twaren.net/Unix/Web/apache/maven/maven-3/3.3.3/binaries/apache-
maven-3.3.3-bin.tar.gz -O - | tar -xz  
# WORKDIR /usr/local/bin  
# RUN ln -s ../apache-maven-3.3.3/bin/mvn .  
ENV MAVEN_VERSION 3.3.3  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
  
USER smallufo  
  

