FROM java:8  
  
MAINTAINER Arpan Chaudhury <arpanchaudhury@gmail.com>  
  
ENV SCALA_VERSION 2.11.8  
ENV SBT_VERSION 0.13.12  
  
RUN wget -nv
"http://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.deb"
&& \  
dpkg -i scala-${SCALA_VERSION}.deb && \  
apt-get update && \  
apt-get install scala && \  
rm scala-${SCALA_VERSION}.deb && \  
\  
wget -nv "https://dl.bintray.com/sbt/debian/sbt-${SBT_VERSION}.deb" && \  
dpkg -i sbt-${SBT_VERSION}.deb && \  
apt-get update && \  
apt-get install sbt && \  
rm sbt-${SBT_VERSION}.deb && \  
\  
sbt version  

