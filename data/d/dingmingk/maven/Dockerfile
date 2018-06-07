FROM java:openjdk-8-jdk  
MAINTAINER dingmingk <dingmingk@gmail.com>  
  
ENV MAVEN_VERSION 3.3.9  
ENV MAVEN_HOME /usr/share/maven  
  
RUN mkdir -p $MAVEN_HOME \  
&& curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC $MAVEN_HOME \--strip-components=1  
  
ENV PATH $PATH:$MAVEN_HOME/bin  
WORKDIR /project  
  
VOLUME /root/.m2  
  
ENTRYPOINT ["mvn"]  
CMD ["-h"]  

