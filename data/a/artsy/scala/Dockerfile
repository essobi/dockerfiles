FROM openjdk:8  
  
ENV SCALA_VERSION=2.12.3 \  
SBT_VERSION=0.13.15  
  
RUN apt-get update -qq && apt-get install -y curl postgresql-client  
RUN cd "/tmp" && \  
curl -q -L -O www.scala-lang.org/files/archive/scala-$SCALA_VERSION.deb && \  
dpkg -i scala-$SCALA_VERSION.deb && \  
curl -q -L -O
https://bintray.com/artifact/download/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN scala -version && \  
sbt about  

