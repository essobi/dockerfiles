FROM debian:latest  
MAINTAINER Dung Vo [cdung.vo@gmail.com]  
  
USER root  
  
# noninteractive Debian frontend  
ENV DEBIAN_FRONTEND noninteractive  
  
# Java version  
ENV JAVA_VERSION 8u45  
  
# Maven version  
#ENV MAVEN_VERSION 3.2.5  
# Install nano, net-tools  
RUN apt-get update && apt-get install -y nano net-tools  
  
# Add packages  
#COPY packages/apache-maven-$MAVEN_VERSION-bin.tar.gz /tmp/apache-
maven-$MAVEN_VERSION-bin.tar.gz  
COPY packages/jdk-$JAVA_VERSION-linux-x64.tar.gz /tmp/jdk-$JAVA_VERSION-
linux-x64.tar.gz  
  
# Install Java 8  
RUN cd /tmp \  
&& tar xzf jdk-$JAVA_VERSION-linux-x64.tar.gz \  
&& rm jdk-$JAVA_VERSION-linux-x64.tar.gz \  
&& mv jdk1.8.0_45 /opt/\  
&& cd /opt \  
&& ln -s jdk1.8.0_45 jdk \  
&& update-alternatives --install /usr/bin/java java /opt/jdk/bin/java 10 \  
&& update-alternatives --install /usr/bin/javac javac /opt/jdk/bin/javac 10 \  
&& update-alternatives --install /usr/bin/jps jps /opt/jdk/bin/jps 10 \  
&& update-alternatives --set java /opt/jdk/bin/java \  
&& update-alternatives --set javac /opt/jdk/bin/javac \  
&& update-alternatives --set jps /opt/jdk/bin/jps  
ENV JAVA_HOME /opt/jdk  
  
# Install maven3  
#RUN cd /tmp \  
# && tar xzf apache-maven-$MAVEN_VERSION-bin.tar.gz \  
# && rm apache-maven-$MAVEN_VERSION-bin.tar.gz \  
# && mv apache-maven-$MAVEN_VERSION /opt/apache-maven-$MAVEN_VERSION-bin \  
# && cd /opt \  
# && ln -s apache-maven-$MAVEN_VERSION maven  
#ADD mvn /opt/maven/bin/mvn  
#ADD settings.xml /opt/maven/conf/settings.xml  
#ENV MAVEN_HOME /opt/maven  
#ENV PATH $MAVEN_HOME/bin:$PATH  
  
ENV PATH $JAVA_HOME/bin:$PATH  
  
CMD ["/bin/bash"]  
  

