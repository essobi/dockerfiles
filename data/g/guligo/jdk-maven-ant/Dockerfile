FROM debian:jessie  
  
USER root  
RUN apt-get update  
RUN apt-get install -y wget  
  
############  
# Oracle JDK  
############  
# Preparation  
ENV JAVA_VERSION 8u45  
ENV JAVA_BUILD 14  
ENV JAVA_HOME /etc/jdk-${JAVA_VERSION}-b${JAVA_BUILD}  
  
# Installation  
RUN cd /tmp  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}-b${JAVA_BUILD}/jdk-${JAVA_VERSION}-linux-x64.tar.gz  
RUN mkdir jdk-${JAVA_VERSION}-linux-x64  
RUN tar -zxvf jdk-${JAVA_VERSION}-linux-x64.tar.gz --directory
jdk-${JAVA_VERSION}-linux-x64 --strip-components=1  
RUN mv jdk-${JAVA_VERSION}-linux-x64 ${JAVA_HOME}  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
# Cleanup  
RUN rm jdk-${JAVA_VERSION}-linux-x64.tar.gz  
RUN unset JAVA_VERSION  
  
#######  
# Maven  
#######  
# Preparation  
ENV MAVEN_VERSION 3.2.3  
ENV MAVEN_HOME /etc/maven-${MAVEN_VERSION}  
  
# Installation  
RUN cd /tmp  
RUN wget
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz  
RUN mkdir maven-${MAVEN_VERSION}  
RUN tar -zxvf apache-maven-${MAVEN_VERSION}-bin.tar.gz --directory
maven-${MAVEN_VERSION} \--strip-components=1  
RUN mv maven-${MAVEN_VERSION} ${MAVEN_HOME}  
ENV PATH ${PATH}:${MAVEN_HOME}/bin  
  
# Cleanup  
RUN rm apache-maven-${MAVEN_VERSION}-bin.tar.gz  
RUN unset MAVEN_VERSION  
  
#####  
# Ant  
#####  
# Preparation  
ENV ANT_VERSION 1.9.5  
ENV ANT_HOME /etc/ant-${ANT_VERSION}  
  
# Installation  
RUN cd /tmp  
RUN wget http://www.us.apache.org/dist/ant/binaries/apache-
ant-${ANT_VERSION}-bin.tar.gz  
RUN mkdir ant-${ANT_VERSION}  
RUN tar -zxvf apache-ant-${ANT_VERSION}-bin.tar.gz --directory
ant-${ANT_VERSION} \--strip-components=1  
RUN mv ant-${ANT_VERSION} ${ANT_HOME}  
ENV PATH ${PATH}:${ANT_HOME}/bin  
  
# Cleanup  
RUN rm apache-ant-${ANT_VERSION}-bin.tar.gz  
RUN unset ANT_VERSION  
  
#########  
# Testing  
#########  
RUN env  
RUN java -version  
RUN javac -version  
RUN mvn -version  
RUN ant -version  
  

