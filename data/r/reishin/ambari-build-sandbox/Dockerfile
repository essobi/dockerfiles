FROM ubuntu:17.10  
MAINTAINER hapy.lestat@gmail.com  
  
SHELL ["/bin/bash","-c"]  
  
ENV SANDBOX_DIR=/var/lib/sandbox  
  
# base system requirements, putting at top to avoid re-build layers  
COPY helpers/get_java.sh ${SANDBOX}/helpers/get_java.sh  
COPY helpers/get_java_parser.py ${SANDBOX}/helpers/get_java_parser.py  
  
# rpm required to build rpm packages  
RUN apt-get update &&\  
apt-get install curl git unzip rpm -y &&\  
apt-get clean  
  
# gcc and python-dev needed for ambari-metrics to build psutils and eat around
190 Mb :(  
RUN apt-get update &&\  
apt-get install --no-install-recommends python2.7-minimal python-pip
python3-minimal python3-pip -y &&\  
apt-get install gcc python-dev -y &&\  
apt-get clean  
  
# Java, Maven versions  
ARG JAVA_VER=8u161  
ARG MVN_VERSION=3.5.2  
ARG JAVA_ROOT_DIR=/usr/jdk  
  
ENV JAVA_HOME=${JAVA_ROOT_DIR}/${JAVA_VER}  
ENV
PATH=${PATH}:${JAVA_HOME}/bin:${JAVA_HOME}/db/bin:${JAVA_HOME}/jre/bin:${SANDBOX_DIR}  
ENV MAVEN_OPTS -Xmx2048m -Djava.awt.headless=true  
  
# Java binary  
RUN mkdir /usr/jdk &&\  
cd /usr/jdk &&\  
bash ${SANDBOX}/helpers/get_java.sh ${JAVA_VER}
jdk-${JAVA_VER}-linux-x64.tar.gz &&\  
mkdir ${JAVA_VER} &&\  
tar xf jdk-${JAVA_VER}-linux-x64.tar.gz -C ${JAVA_VER} \--strip-components
1&&\  
rm -f jdk-${JAVA_VER}-linux-x64.tar.gz &&\  
touch ${JAVA_ROOT_DIR}/accepted-oracle-license-v1-1&&\  
update-alternatives --install "/usr/bin/java" "java" "${JAVA_HOME}/bin/java"
1&&\  
update-alternatives --install "/usr/bin/javac" "javac"
"${JAVA_HOME}/bin/javac" 1  
  
# Maven binary  
RUN cd /opt &&\  
curl
http://archive.apache.org/dist/maven/maven-3/${MVN_VERSION}/binaries/apache-
maven-${MVN_VERSION}-bin.tar.gz -o apache-maven-${MVN_VERSION}-bin.tar.gz &&\  
tar xf apache-maven-${MVN_VERSION}-bin.tar.gz && rm -f apache-
maven-${MVN_VERSION}-bin.tar.gz &&\  
update-alternatives --install "/usr/bin/mvn" "mvn" "/opt/apache-
maven-${MVN_VERSION}/bin/mvn" 1  
  
# building tools  
RUN pip install setuptools  
  
# pydebug egg: https://plugins.jetbrains.com/plugin/631-python  
# 173.4127—173.*: https://plugins.jetbrains.com/plugin/download?updateId=41832  
RUN cd /tmp &&\  
curl -L https://plugins.jetbrains.com/plugin/download?updateId=41832 -o
egg.zip &&\  
unzip egg.zip &&\  
python2 -m easy_install python/pycharm-debug.egg &&\  
#python3 -m easy_install python/pycharm-debug-py3k.egg &&\  
rm -rf /tmp/python &&\  
rm -f egg.zip  
  
VOLUME ["/root/.m2"]  
VOLUME ["/root/ambari"]  
  
CMD ["/bin/bash"]

