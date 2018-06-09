FROM tedneward/java  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
ENV MAVEN_VER=3.5.0  
RUN mkdir -p /usr/local/maven /usr/local/maven/ref \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz
https://apache.osuosl.org/maven/maven-3/${MAVEN_VER}/binaries/apache-
maven-${MAVEN_VER}-bin.tar.gz \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/local/maven --strip-components=1
\  
&& rm -f /tmp/apache-maven.tar.gz \  
&& ln -s /usr/local/maven/bin/mvn /usr/local/bin/mvn  
  
ENV MAVEN_HOME /usr/local/maven  
  
ENTRYPOINT ["/bin/bash"]  

