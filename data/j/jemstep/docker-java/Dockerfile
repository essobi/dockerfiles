FROM ubuntu:trusty  
  
# Install Oracle Java 8  
ENV JAVA_VER 8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ENV SBT_VERSION 0.13.12  
ENV SBT_TGZ sbt-${SBT_VERSION}.tgz  
ENV SBT_URL https://dl.bintray.com/sbt/native-
packages/sbt/${SBT_VERSION}/${SBT_TGZ}  
ENV SBT_BASE /usr/lib/sbt  
ENV SBT_HOME ${SBT_BASE}/${SBT_VERSION}  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \  
apt-get update && \  
apt-get install -y --force-yes --no-install-recommends software-properties-
common sudo openssh-client gnupg2 wget curl ca-certificates && \  
mkdir -p ${SBT_BASE} && \  
wget --no-check-certificate -O ${SBT_BASE}/${SBT_TGZ} ${SBT_URL} && \  
cd ${SBT_BASE} && \  
tar zxvf ${SBT_TGZ} && \  
mv sbt ${SBT_VERSION} && \  
echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1
select true | sudo /usr/bin/debconf-set-selections && \  
apt-get install -y --force-yes --no-install-recommends oracle-
java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default oracle-
java${JAVA_VER}-unlimited-jce-policy && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists && \  
rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer && \  
rm -rf ${JAVA_HOME}/ct.sym && \  
rm -rf ${JAVA_HOME}/src.zip && \  
rm -rf ${JAVA_HOME}/javafx-src.zip && \  
rm -rf ${JAVA_HOME}/lib/visualvm && \  
rm -rf ${JAVA_HOME}/lib/missioncontrol  

