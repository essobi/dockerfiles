FROM ubuntu:16.04  
MAINTAINER Taewan Kim <taewanme@gmail.com>  
  
USER root  
  
ENV MV 8  
ENV UV 102  
ENV BV 14  
ENV JDK_TAR_NAME jdk-${MV}u${UV}-linux-x64.tar.gz  
ENV JAVA_DIR_NAME jdk1.${MV}.0_${UV}  
ENV INSTALL_HOME /usr/local/java  
ENV JAVA_HOME_DIR ${INSTALL_HOME}/${JAVA_DIR_NAME}  
ENV DOWNLOAD_URL https://edelivery.oracle.com/otn-
pub/java/jdk/${MV}u${UV}-b${BV}/${JDK_TAR_NAME}  
ENV JAVA_HOME ${JAVA_HOME_DIR}  
ENV MAVEN_HOME ${INSTALL_HOME}/apache-maven-3.3.9  
ENV ANT_HOME ${INSTALL_HOME}/apache-ant-1.9.7  
ENV PATH $PATH:$MAVEN_HOME/bin:$JAVA_HOME/bin:$ANT_HOME/bin  
  
RUN apt-get update \  
&& apt-get install -y curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -L -O -H "Cookie: oraclelicense=accept-securebackup-cookie" -k
${DOWNLOAD_URL} && \  
mkdir -p ${INSTALL_HOME} && \  
tar xvfz ./${JDK_TAR_NAME} -C ${INSTALL_HOME} && \  
rm -f ./${JDK_TAR_NAME}  
RUN curl -L -O
http://apache.mirror.cdnetworks.com/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz && \  
tar xvfz ./*.tar.gz -C ${INSTALL_HOME} && \  
rm -f ./*.tar.gz  
RUN curl -L -O http://apache.mirror.cdnetworks.com/ant/binaries/apache-
ant-1.9.7-bin.tar.gz && \  
tar xvfz ./*.tar.gz -C ${INSTALL_HOME} && \  
rm -f ./*.tar.gz  
  
RUN update-alternatives --install "/usr/bin/java" "java"
"${JAVA_HOME_DIR}/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javac" "javac"
"${JAVA_HOME_DIR}/bin/javac" 1 && \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"${JAVA_HOME_DIR}/bin/javaws" 1  

