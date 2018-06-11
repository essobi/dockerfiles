FROM ubuntu:14.04.4  
MAINTAINER Lloyd H. Meinholz <meinholz@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV MAVEN_VERSION 3.3.9  
ENV GROOVY_VERSION 2.4.5  
  
COPY download-maven.sh /tmp/download-maven.sh  
COPY download-groovy.sh /tmp/download-groovy.sh  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
build-essential \  
ca-certificates \  
lsb-release \  
libssl-dev \  
curl \  
git \  
unzip \  
rlwrap \  
libfontconfig \  
libfontconfig-dev \  
python-software-properties \  
software-properties-common && \  
rm -rf /var/lib/apt/lists/* && \  
locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales && \  
# Install Oracle Java from PPA & set Oracle Java as the default  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get -y install oracle-java8-installer && apt-get clean && \  
update-java-alternatives -s java-8-oracle && \  
echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc && \  
# Install maven  
/tmp/download-maven.sh && \  
tar xf /tmp/apache-maven-${MAVEN_VERSION}-bin.tar.gz -C /opt && \  
mv /opt/apache-maven-${MAVEN_VERSION} /opt/maven-${MAVEN_VERSION} && \  
echo "export M2_HOME=/opt/maven-${MAVEN_VERSION}" >> ~/.bashrc && \  
echo "export PATH=/opt/maven-${MAVEN_VERSION}/bin:\$PATH" >> ~/.bashrc && \  
# Install groovy  
/tmp/download-groovy.sh && \  
unzip /tmp/apache-groovy-sdk-${GROOVY_VERSION}.zip -d /opt && \  
echo "export GROOVY_HOME=/opt/groovy-${GROOVY_VERSION}" >> ~/.bashrc && \  
echo "export PATH=/opt/groovy-${GROOVY_VERSION}/bin:\$PATH" >> ~/.bashrc  
  
CMD ["/bin/bash"]  

