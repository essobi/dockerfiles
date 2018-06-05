#  
# Oracle JDK 8 Dockerfile  
#  
# https://bitbucket.org/nuccess/docker-nuclos-jdk  
#  
FROM ubuntu:14.04  
ARG DOWNLOAD_URL=http://download.oracle.com/otn-
pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jdk-8u151-linux-x64.tar.gz  
ARG DOWNLOAD_HASH=774d8cb584d9ebedef8eba9ee2dfe113  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle  
  
WORKDIR /usr/lib/jvm  
  
RUN \  
apt-get update && \  
apt-get install -y wget curl rsync && \  
rm -rf /var/lib/apt/lists/*  
RUN \  
wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" $DOWNLOAD_URL  
RUN \  
export DOWNLOAD_FILE="${DOWNLOAD_URL##*/}" && \  
echo "Checking downloaded $DOWNLOAD_FILE ... " && \  
test `md5sum $DOWNLOAD_FILE | awk '{ print $1 }'` = $DOWNLOAD_HASH && \  
tar xzf $DOWNLOAD_FILE && \  
rm $DOWNLOAD_FILE && \  
export JDK_DIR=$(find . -maxdepth 1 -iname "jdk*" -type d) && \  
mv $JDK_DIR java-8-oracle  
  
RUN \  
update-alternatives --install /usr/bin/java java $JAVA_HOME/jre/bin/java 2000
&& \  
update-alternatives --install /usr/bin/javac javac $JAVA_HOME/bin/javac 2000  
  
RUN \  
echo "export PATH=$PATH:$JAVA_HOME/bin:$JAVA_HOME/jre/bin" >
/etc/profile.d/oraclejdk.sh && \  
echo "export JAVA_HOME=$JAVA_HOME" >> /etc/profile.d/oraclejdk.sh

