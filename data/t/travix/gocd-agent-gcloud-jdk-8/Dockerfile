FROM travix/gocd-agent-gcloud:18.5.0  
  
MAINTAINER Travix  
  
ENV MAVEN_VERSION=3.3.9  
# install packages  
RUN echo "deb http://http.debian.net/debian jessie-backports main" | tee
/etc/apt/sources.list.d/jessie-backports.list \  
&& apt-get update \  
&& apt-get install -y -t jessie-backports \  
openjdk-8-jre-headless \  
openjdk-8-jre \  
openjdk-8-jdk-headless \  
openjdk-8-jdk \  
&& curl -fSL
"http://apache.cs.uu.nl/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.zip" -o apache-maven.zip \  
&& unzip apache-maven.zip -d /opt \  
&& rm -f apache-maven.zip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& curl -fSL "https://downloads.gradle.org/distributions/gradle-2.14-bin.zip"
-o gradle-2.14-bin.zip \  
&& unzip gradle-2.14-bin.zip -d /opt \  
&& rm -f gradle-2.14-bin.zip  
  
ENV GRADLE_HOME=/opt/gradle-2.14  
  
ENV PATH /opt/apache-maven-$MAVEN_VERSION/bin:/opt/gradle-2.14/bin:$PATH

