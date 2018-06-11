FROM google/debian:wheezy  
  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV HADOOP_VERSION 2.6.0  
ENV HADOOP_INSTALL_DIR /etc/hadoop  
  
  
  
# install needed debian packages & clean up  
RUN apt-get update && \  
apt-get install -y --no-install-recommends curl tar ca-certificates
openjdk-7-jre supervisor python2.7 && \  
apt-get -q -y install openssh-server && \  
mkdir -p /var/run/sshd && \  
echo 'root:passw0rd' | chpasswd && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
# download and extract hadoop  
RUN mkdir -p ${HADOOP_INSTALL_DIR} && \  
curl -L --silent
http://www.eu.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz
| tar -xz --strip=1 -C ${HADOOP_INSTALL_DIR}  
  
RUN sed -i s/"files dns"/"dns files"/ /etc/nsswitch.conf  
  
WORKDIR /etc/hadoop  
  

