FROM ubuntu:14.04  
MAINTAINER Thiadmer Sikkema "t.sikkema@voipq.nl"  
RUN apt-get update && apt-get install -y wget git curl zip monit  
  
###  
# Install Oracle JDK 8  
#  
RUN echo "# Installing Oracle JDK 8" && \  
sudo apt-get install -y software-properties-common debconf-utils && \  
sudo add-apt-repository -y ppa:webupd8team/java && \  
sudo apt-get update && \  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| sudo debconf-set-selections && \  
sudo apt-get install -y oracle-java8-installer  
  
###  
# Install Maven  
#  
ENV MAVEN_VERSION 3.5.2  
ENV MAVEN_ROOT /var/lib/maven  
ENV MAVEN_HOME $MAVEN_ROOT/apache-maven-$MAVEN_VERSION  
ENV MAVEN_OPTS -Xms256m -Xmx512m -Dmaven.repo.local=/tmp/mvn-repo-cache  
VOLUME /tmp/mvn-repo-cache  
  
RUN echo "# Installing Maven " && echo ${MAVEN_VERSION} && \  
wget --no-verbose -O /tmp/apache-maven-$MAVEN_VERSION.tar.gz \  
http://ftp.tudelft.nl/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz && \  
mkdir -p $MAVEN_ROOT && \  
tar xzf /tmp/apache-maven-$MAVEN_VERSION.tar.gz -C $MAVEN_ROOT && \  
ln -s $MAVEN_HOME/bin/mvn /usr/local/bin && \  
rm -f /tmp/apache-maven-$MAVEN_VERSION.tar.gz  
  
###  
# NodeJS  
#  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \  
sudo apt-get install -y nodejs  

