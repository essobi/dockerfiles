FROM ubuntu:xenial  
MAINTAINER "Christian Kniep <christian@qnib.org>"  
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/  
RUN apt-get update \  
&& apt-get install -y openjdk-8-jdk  
  
ENV SCALA_VERSION 2.11.7  
ENV SBT_VERSION 0.13.8  
# Install Scala  
## Piping curl directly in tar  
RUN apt-get install -y curl fakeroot \  
&& curl -fsL
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C /root/ \  
&& echo >> /root/.bashrc \  
&& echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc  
  
# Install sbt  
RUN curl -L -o sbt-$SBT_VERSION.deb
https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb \  
&& dpkg -i sbt-$SBT_VERSION.deb \  
&& rm sbt-$SBT_VERSION.deb \  
&& apt-get update \  
&& apt-get install sbt  
RUN sbt clean  
  

