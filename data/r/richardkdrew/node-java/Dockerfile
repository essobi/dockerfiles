# DOCKER-VERSION 1.9.1  
#  
# Node.js (w/ Bower & Grunt and including Java) Dockerfile  
#  
# https://github.com/richardkdrew/docker-node-java  
#  
  
FROM node:5.10.1  
  
MAINTAINER Richard Drew <richardkdrew@gmail.com>  
  
# Install Bower & Grunt  
RUN npm install -g bower grunt-cli  
  
# JAVA - http://download.oracle.com/otn-
pub/java/jdk/8u60-b27/jdk-8u60-linux-x64.tar.gz  
ENV JAVA_VERSION_MAJOR=1 \  
JAVA_VERSION_MINOR=8 \  
JAVA_VERSION_BUILD=27 \  
JAVA_VERSION_UPDATE=60 \  
JAVA_HOME=/opt/lib/java-oracle/jdk \  
DEBIAN_FRONTEND=noninteractive  
  
ENV
JAVA_VERSION=${JAVA_VERSION_MAJOR}.${JAVA_VERSION_MINOR}.0_${JAVA_VERSION_UPDATE}  
ENV PATH ${JAVA_HOME}/bin:$PATH  
  
# install dependencies  
RUN buildDeps='curl ca-certificates' \  
&& apt-get update \  
&& apt-get install -y $buildDeps --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
# install Java  
RUN mkdir -p ${JAVA_HOME} \  
&& curl -sSL -o /JDK-${JAVA_VERSION}.tar.gz http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MINOR}u${JAVA_VERSION_UPDATE}-b${JAVA_VERSION_BUILD}/jdk-${JAVA_VERSION_MINOR}u${JAVA_VERSION_UPDATE}-linux-x64.tar.gz
-H "Cookie: oraclelicense=accept-securebackup-cookie" \  
&& tar zxf /JDK-${JAVA_VERSION}.tar.gz -C /opt/lib \  
&& rm -f /JDK-${JAVA_VERSION}.tar.gz \  
&& mv /opt/lib/jdk${JAVA_VERSION}/* ${JAVA_HOME} \  
#&& ln -s /opt/lib/java-oracle/bin/java /usr/bin/java \  
# do some clean-up  
&& apt-get purge -y --auto-remove $buildDeps \  
# do some additional config  
&& update-alternatives --install /usr/bin/java java ${JAVA_HOME}/bin/java
20000 && update-alternatives --install /usr/bin/javac javac
${JAVA_HOME}/bin/javac 20000  
  
CMD ["java"]

