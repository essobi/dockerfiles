# Ubuntu 16.04 LTS # Oracle Java 1.8.0_92 64 bit  
# Maven 3.3.9  
FROM ubuntu:16.04  
# this is a non-interactive automated build - avoid some warning messages  
ENV DEBIAN_FRONTEND noninteractive  
# Enable 32 bit architecture for launch4J  
RUN dpkg --add-architecture i386  
# update dpkg repositories  
RUN apt-get update  
# install wget  
RUN apt-get install -y wget libc6:i386 libstdc++6:i386  
# get maven 3.3.9  
RUN wget --no-verbose -O /tmp/apache-maven-3.3.9.tar.gz
http://archive.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz  
# verify checksum  
RUN echo "516923b3955b6035ba6b0a5b031fbd8b /tmp/apache-maven-3.3.9.tar.gz" |
md5sum -c  
# install maven  
RUN tar xzf /tmp/apache-maven-3.3.9.tar.gz -C /opt/  
RUN ln -s /opt/apache-maven-3.3.9 /opt/maven  
RUN ln -s /opt/maven/bin/mvn /usr/local/bin  
RUN rm -f /tmp/apache-maven-3.3.9.tar.gz  
ENV MAVEN_HOME /opt/maven  
# remove download archive files  
RUN apt-get clean  
# set shell variables for java installation  
ENV java_version 1.8.0_92  
ENV filename jdk-8u92-linux-x64.tar.gz  
ENV downloadlink http://download.oracle.com/otn-
pub/java/jdk/8u92-b14/$filename  
# download java, accepting the license agreement  
RUN wget --no-cookies --header "Cookie: oraclelicense=accept-securebackup-
cookie" -O /tmp/$filename $downloadlink  
# unpack java  
RUN mkdir /opt/oracle-java && tar -zxf /tmp/$filename -C /opt/oracle-java/  
ENV JAVA_HOME /opt/oracle-java/jdk$java_version  
ENV PATH $JAVA_HOME/bin:$PATH  
# configure symbolic links for the java and javac executables  
RUN update-alternatives --install /usr/bin/java java $JAVA_HOME/bin/java 20000
&& update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac
20000

