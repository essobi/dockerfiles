FROM ubuntu:14.04  
  
MAINTAINER Marcelo Teixeira Monteiro  
  
ENV LC_ALL C  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
ENV INITRD no  
ENV MAVEN_VER 3.3.1  
ENV MAVEN_ROOT_PATH http://www.us.apache.org/dist/maven/maven-3  
  
WORKDIR /root  
  
RUN apt-get install -y software-properties-common curl && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer oracle-java8-set-default && \  
apt-get clean && \  
rm -rf /var/cache/oracle-jdk*-installer  
  
RUN curl -L \--progress-bar $MAVEN_ROOT_PATH/$MAVEN_VER/binaries/apache-
maven-$MAVEN_VER-bin.tar.gz | tar xz -C /opt && \  
ln -s /opt/apache-maven-$MAVEN_VER/bin/mvn /usr/bin && \  
rm -f apache-maven-$MAVEN_VER-bin.tar.gz  

