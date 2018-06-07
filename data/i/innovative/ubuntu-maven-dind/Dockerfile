FROM ubuntu:16.04  
MAINTAINER Innovative People <contact@inpglobal.com>  
  
# Let's start with some basic stuff.  
RUN apt-get update -qq && apt-get install -qqy --no-install-recommends \  
apt-transport-https ca-certificates curl tzdata \  
locales iptables curl python-pip git sed unzip netcat wget && \  
apt-get upgrade -y  
  
# Install Docker from Docker Inc. repositories.  
RUN curl -sSL https://get.docker.com/ | sh  
  
# JDK version info from  
# http://www.oracle.com/technetwork/java/javase/downloads/index.html  
ENV DEBIAN_FRONTEND noninteractive  
ENV VERSION 8  
ENV UPDATE 161  
ENV BUILD 12  
ENV SIG 2f38c3b165be4555a1fa6e98c45e0808  
ENV JAVA_HOME /usr/lib/jvm/java-${VERSION}-oracle  
ENV JRE_HOME ${JAVA_HOME}/jre  
ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF-8  
# http://download.oracle.com/otn-
pub/java/jdk/8u161-b12/2f38c3b165be4555a1fa6e98c45e0808/jdk-8u161-linux-x64.tar.gz  
RUN locale-gen en_US.UTF-8 && \  
localedef -i en_US -c -f UTF-8 en_US.UTF-8 && \  
curl -v --location --retry 3 --capath /etc/ssl/certs \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-
pub/java/jdk/"${VERSION}"u"${UPDATE}"-b"${BUILD}"/"${SIG}"/jdk-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz
\  
| tar xz -C /tmp && \  
mkdir -p /usr/lib/jvm && mv /tmp/jdk1.${VERSION}.0_${UPDATE} "${JAVA_HOME}"  
  
# Make Oracle Java default && install docker-compose  
RUN update-alternatives --install "/usr/bin/java" "java"
"${JRE_HOME}/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"${JRE_HOME}/bin/javaws" 1 && \  
update-alternatives --install "/usr/bin/javac" "javac"
"${JAVA_HOME}/bin/javac" 1 && \  
update-alternatives --set java "${JRE_HOME}/bin/java" && \  
update-alternatives --set javaws "${JRE_HOME}/bin/javaws" && \  
update-alternatives --set javac "${JAVA_HOME}/bin/javac" && \  
pip install --upgrade setuptools && \  
pip install --upgrade pip && \  
pip install docker-compose  
  
ARG MAVEN_VERSION=3.5.2  
ARG USER_HOME_DIR="/root"  
ARG SHA=707b1f6e390a65bde4af4cdaf2a24d45fc19a6ded00fff02e91626e3e42ceaff  
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries  
  
RUN mkdir -p /usr/share/maven /usr/share/maven/ref && \  
curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-
maven-${MAVEN_VERSION}-bin.tar.gz && \  
echo "${SHA} /tmp/apache-maven.tar.gz" | sha256sum -c - && \  
tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 &&
\  
rm -f /tmp/apache-maven.tar.gz && \  
ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
# Remove apt cache  
RUN apt-get autoclean && apt-get --purge -y autoremove && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure timezone && locale  
RUN ln -fs /usr/share/zoneinfo/Europe/Moscow /etc/localtime && \  
echo "Europe/Moscow" > /etc/timezone && \  
dpkg-reconfigure -f noninteractive tzdata && \  
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"' > /etc/default/locale && \  
update-locale LANG="en_US.UTF-8" LANGUAGE="en_US" && \  
dpkg-reconfigure --frontend=noninteractive locales  
  
# Install the magic wrapper.  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
# Define additional metadata for our image.  
VOLUME /var/lib/docker  
CMD ["wrapdocker"]  

