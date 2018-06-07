FROM openjdk:8  
ENV SCALA_VERSION 2.11.12  
ENV SBT_VERSION 0.13.16  
ENV SBT_OPTS=-Duser.home=/work  
  
RUN mkdir -p /work  
  
# Scala expects this file  
RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release  
  
# Install Scala  
RUN curl -fsL
"http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz"
\  
| tar xzf - -C /usr/local \--strip-components=1  
  
# Install SBT  
RUN \  
curl -fsL -o sbt-$SBT_VERSION.deb
https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
apt-get update && \  
apt-get install sbt && \  
sbt sbtVersion  
  
RUN chmod a+w /work -R  
  
# add git  
RUN apt-get install git  
  
VOLUME /work  
WORKDIR /work  
  
CMD ["sbt"]  

