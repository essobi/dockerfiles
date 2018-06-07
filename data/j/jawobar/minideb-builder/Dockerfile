FROM bitnami/minideb  
  
ENV \  
JAVA_HOME=/usr/lib/jvm/java-10-openjdk-amd64 \  
GRADLE_VERSION=4.6 \  
GRADLE_HOME=/usr/local/gradle  
  
# JDK  
RUN \  
echo 'deb http://deb.debian.org/debian unstable main' >
/etc/apt/sources.list.d/unstable.list && \  
ln -svT $JAVA_HOME/bin/java /usr/local/bin/java && \  
apt-get update && \  
install_packages openjdk-10-jdk-headless  
  
# GRADLE  
RUN \  
cd /usr/local && \  
install_packages wget unzip && \  
wget https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip
&& \  
unzip gradle-$GRADLE_VERSION-bin.zip && \  
rm -f gradle-$GRADLE_VERSION-bin.zip && \  
ln -s gradle-$GRADLE_VERSION gradle  
  
# AWS CLI  
RUN \  
install_packages python-pip && \  
pip install wheel setuptools && \  
pip install --upgrade awscli  
  
# CLEANUP  
RUN \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/man/*  
  
ENV \  
PATH=${PATH}:${JAVA_HOME}/bin:${GRADLE_HOME}/bin  

