FROM sgrio/java-oracle:jdk_8  
MAINTAINER Dealermade  
  
ENV SBT_VERSION 1.0.4  
RUN \  
curl -L -o sbt-$SBT_VERSION.deb
https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
apt-get update && \  
apt-get install sbt && \  
sbt sbtVersion  
  
CMD ["sbt"]  

