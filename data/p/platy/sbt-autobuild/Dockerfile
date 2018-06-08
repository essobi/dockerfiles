FROM ubuntu:14.04  
MAINTAINER Mike Bush <mpbush@gmail.com>  
  
# get apt repo lists  
RUN apt-get update  
  
# wget for future installs  
RUN apt-get install -y wget  
  
# java openjdk7  
RUN apt-get install --no-install-recommends -y \  
openjdk-7-jdk  
  
# scala 2.11  
RUN wget http://www.scala-lang.org/files/archive/scala-2.11.0.deb && \  
dpkg -i scala-2.11.0.deb && \  
rm scala-2.11.0.deb  
  
# sbt 0.13  
RUN wget http://dl.bintray.com/sbt/debian/sbt-0.13.2.deb && \  
dpkg -i sbt-0.13.2.deb && \  
rm sbt-0.13.2.deb  
  
# update sbt packages, sbt fails if there is no project, this is the simplest
way I’ve found to make it succeed so far  
RUN mkdir /tempproject && \  
echo 'object Hi { def main(args: Array[String]) = println("Hi!") }' >
/tempproject/hw.scala && \  
cd /tempproject && \  
sbt update && \  
cd && \  
rm -r /tempproject  
  
ONBUILD ADD project /app/project  
ONBUILD ADD src /app/src  
ONBUILD ADD build.sbt /app/  
  
ONBUILD WORKDIR /app  
ONBUILD RUN sbt compile  
  
ONBUILD CMD sbt run  
  

