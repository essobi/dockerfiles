#  
# Maven and SBT with OpenJDK-8 running on Alpine Linux image  
#  
  
FROM java:openjdk-8-jdk-alpine  
MAINTAINER IFlavours's Docker Team <docker@iflavours.nl>  
  
ENV MAVEN_VERSION 3.3.9  
ENV MAVEN_ARCHIVE
http://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz  
ENV MAVEN_HOME /usr/local/maven  
ENV PATH=${PATH}:${MAVEN_HOME}/bin  
  
ENV SBT_VERSION 0.13.12  
ENV SBT_HOME /usr/local/sbt  
ENV PATH=${PATH}:${SBT_HOME}/bin  
ENV SBT_JAR http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz  
RUN apk --update add --no-cache bash wget curl tar git && \  
wget ${MAVEN_ARCHIVE} && \  
tar -xf apache-maven-${MAVEN_VERSION}-bin.tar.gz -C /usr/local && \  
mv /usr/local/apache-maven-${MAVEN_VERSION} /usr/local/maven && \  
rm apache-maven-${MAVEN_VERSION}-bin.tar.gz && \  
wget ${SBT_JAR} && \  
tar -xf sbt-$SBT_VERSION.tgz -C /usr/local && \  
echo -ne "- with sbt sbt-$SBT_VERSION\n" >> /root/.built && \  
rm sbt-$SBT_VERSION.tgz && \  
sbt sbt-version  
  
VOLUME [ "/code" ]  
WORKDIR /code  

