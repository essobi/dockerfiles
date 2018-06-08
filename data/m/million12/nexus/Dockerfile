FROM centos:centos7  
MAINTAINER Przemyslaw Ozgo linux@ozgo.info  
  
ENV JAVA_HOME /usr/lib/jvm/jre \  
NEXUS_WEBAPP_CONTEXT_PATH /nexus  
  
COPY container-files/ /  
  
RUN \  
rpm --rebuilddb && yum clean all && \  
yum install -y \  
java-1.8.0-openjdk-devel \  
which \  
telnet \  
unzip \  
openssh-server \  
sudo \  
openssh-clients \  
iputils \  
iproute \  
httpd-tools \  
wget \  
tar; \  
yum clean all && \  
mkdir -p /opt/sonatype-nexus /opt/sonatype-work && \  
wget -O /tmp/nexus-latest-bundle.tar.gz
http://www.sonatype.org/downloads/nexus-latest-bundle.tar.gz && \  
tar xzvf /tmp/nexus-latest-bundle.tar.gz -C /opt/sonatype-nexus --strip-
components=1 && \  
rm -f /tmp/nexus-latest-bundle.tar.gz && \  
useradd --user-group --system --home-dir /opt/sonatype-nexus nexus && \  
chown -R nexus:nexus /opt/sonatype-work /opt/sonatype-nexus && \  
chmod +x /opt/start-nexus.sh  
  
CMD ["/opt/start-nexus.sh"]  
USER nexus  
EXPOSE 8081

