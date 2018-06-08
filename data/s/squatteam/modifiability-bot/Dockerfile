#from https://runnable.com/docker/java/dockerize-your-java-application  
FROM phusion/baseimage:0.9.17  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >
/etc/apt/sources.list  
  
RUN apt-get -y update  
#install java  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q python-software-
properties software-properties-common  
  
ENV JAVA_VER 8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C2518248EEA14886 && \  
apt-get update && \  
echo oracle-java${JAVA_VER}-installer shared/accepted-oracle-license-v1-1
select true | sudo /usr/bin/debconf-set-selections && \  
apt-get install -y --force-yes --no-install-recommends oracle-
java${JAVA_VER}-installer oracle-java${JAVA_VER}-set-default && \  
apt-get clean && \  
rm -rf /var/cache/oracle-jdk${JAVA_VER}-installer  
  
RUN update-java-alternatives -s java-8-oracle  
  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> ~/.bashrc  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#copy files to docker  
ADD pcm /home/pcm  
ADD model /home/model  
ADD src /home/src  
ADD lib /home/lib  
ADD lib2 /home/lib2  
ADD lib3 /home/lib3  
ADD pom.xml /home/pom.xml  
  
# Install maven  
ENV MAVEN_VERSION 3.3.9  
RUN mkdir -p /usr/share/maven \  
&& curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
WORKDIR /home  
  
RUN ["mvn", "clean"]  
RUN ["mvn", "initialize"]  
RUN ["mvn", "dependency:resolve"]  
RUN ["mvn", "verify"]  
RUN ["mvn", "package"]  
  
# the jar is not copied anymore but created by maven  
#ADD squat-tool-modifiability.jar /home/squat-tool-modifiability.jar  
ENTRYPOINT java -jar /home/target/squat-tool-modifiability.jar  
  

