FROM java:openjdk-6-jdk  
  
ENV MAVEN_VERSION 3.2.5  
  
RUN curl -fsSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \  
&& ln -s /usr/share/maven/bin/mvnDebug /usr/bin/mvnDebug  
  
ENV MAVEN_HOME /usr/share/maven  
  
CMD ["mvn"]  

