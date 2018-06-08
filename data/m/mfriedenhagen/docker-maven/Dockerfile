FROM openjdk:7-jdk  
  
ARG MAVEN_VERSION=3.3.9  
  
RUN mkdir -p /usr/share/maven \  
&& curl -fsSL
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
| tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
RUN useradd --create-home user \  
&& mkdir -p /home/user/.m2/repository \  
&& chown -R user:user /home/user/.m2 /home/user/.m2/repository  
  
ENV MAVEN_HOME /usr/share/maven  
USER user  
CMD ["mvn", "--version"]

