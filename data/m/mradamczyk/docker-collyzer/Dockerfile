FROM java:openjdk-8-jdk  
MAINTAINER Michał Adamczyk <mr.adamczyk@gmail.com>  
  
ENV MAVEN_VERSION 3.3.9  
RUN mkdir -p /usr/share/maven \  
&& curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
ADD . /usr/share/collyzer  
  
WORKDIR /usr/share/collyzer  
  
RUN mvn install:install-file -Dfile=external/docker-java-3.0.0-SNAPSHOT.jar
-DgroupId=com.github.docker-java -DartifactId=docker-java
-Dversion=3.0.0-SNAPSHOT -Dpackaging=jar -DlocalRepositoryPath=external/repo  
RUN mvn compile  
  
ENTRYPOINT ["./run.sh", "/collyzer-conf", "/collyzer-outdir", "/docker-certs"]  

