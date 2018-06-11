FROM twistedogic/codebox:latest  
MAINTAINER Jordan Li  
ENV XD_BUILD snapshot  
ENV XD_VERSION 1.2.0.BUILD-SNAPSHOT  
ENV HADOOP_VERSION 2.6.0  
ENV HADOOP_INSTALL_DIR /etc/hadoop  
RUN apt-get update -y && \  
apt-get install -y openjdk-7-jre-headless curl tar ca-certificates python2.7
rsync wget unzip && \  
wget http://repo.spring.io/${XD_BUILD}/org/springframework/xd/spring-
xd/${XD_VERSION}/spring-xd-${XD_VERSION}-dist.zip \  
-O /opt/spring-xd-${XD_VERSION}-dist.zip \  
&& unzip /opt/spring-xd-${XD_VERSION}-dist.zip -d /opt/ \  
&& rm /opt/spring-xd-${XD_VERSION}-dist.zip \  
&& ln -s /opt/spring-xd-${XD_VERSION} /opt/spring-xd && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
# download and extract hadoop  
RUN mkdir -p ${HADOOP_INSTALL_DIR} && \  
curl -L --silent
http://www.eu.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
| tar -xz --strip=1 -C ${HADOOP_INSTALL_DIR}  

