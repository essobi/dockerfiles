FROM ubuntu:14.04  
WORKDIR /root  
  
RUN apt-get update && apt-get install -y software-properties-common  
RUN sudo add-apt-repository ppa:webupd8team/java  
RUN apt-get update && echo oracle-java7-installer shared/accepted-oracle-
license-v1-1 select true | /usr/bin/debconf-set-selections && \  
apt-get install -y oracle-java8-installer \  
git \  
openssh-server \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ENV MAVEN_VERSION 3.3.9  
RUN mkdir -p /usr/share/maven \  
&& curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  

