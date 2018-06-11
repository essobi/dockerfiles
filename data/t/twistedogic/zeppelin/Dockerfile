FROM twistedogic/spark-mesos  
MAINTAINER Jordan Li  
ENV ZEPPELIN_DOWNLOAD_URL https://github.com/apache/incubator-
zeppelin/archive/v0.5.0.zip  
ENV SPARK_HOME /opt/spark/  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
RUN apt-get update -y  
RUN apt-get install -y build-essential g++ git wget unzip python2.7 npm
openjdk-7-jdk curl && \  
apt-get clean autoclean && \  
apt-get autoremove --yes && \  
rm -rf /var/lib/{apt,dpkg,cache,log}/  
ENV MAVEN_VERSION 3.3.1  
RUN curl -sSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
RUN git clone https://github.com/apache/incubator-zeppelin.git  
RUN cd incubator-zeppelin \  
git reset --hard 2498e5df12ae8cc1b24375e253df94394710aaf8  
  
RUN cd /incubator-zeppelin && mvn clean package -Pspark-1.4
-Dhadoop.version=2.6.0 -Phadoop-2.6 -Pyarn -DskipTests  
ADD supervisord.conf /etc/supervisord.conf  

