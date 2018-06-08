# Scala, Java, and sbt for Ubuntu 12.04 LTS  
#  
# Version 0.3  
FROM ubuntu:precise  
MAINTAINER Åukasz Budnik lukasz.budnik@gmail.com  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" >
/etc/apt/sources.list  
  
# install add-apt-repository tool  
RUN apt-get install -y python-software-properties  
  
# Java 7 apt repository  
RUN add-apt-repository ppa:webupd8team/java  
  
# install wget for downloading files  
RUN apt-get install -y wget  
  
# Typesafe repo (contains old versions but they have all dependencies we need
later on)  
RUN wget http://apt.typesafe.com/repo-deb-build-0002.deb  
RUN dpkg -i repo-deb-build-0002.deb  
RUN rm -f repo-deb-build-0002.deb  
  
# update apt repositories  
RUN apt-get update  
  
# install Scala 2.10.3, requires OpenJDK 1.6  
# 1) first install prerequisites  
RUN apt-get install -y openjdk-6-jre libjansi-java  
# 2) finally install Scala 2.10.3  
RUN wget http://www.scala-lang.org/files/archive/scala-2.10.3.deb  
RUN dpkg -i scala-2.10.3.deb  
RUN rm -f scala-2.10.3.deb  
  
# upgrade Java to latest 1.7.x  
RUN echo 'debconf shared/accepted-oracle-license-v1-1 select true' | debconf-
set-selections  
RUN apt-get install -y oracle-java7-set-default  
  
# install sbt 0.13.1  
# 1) first install old sbt 0.11.3 from typesafe (old one but comes with all
dependencies)  
RUN apt-get install -y sbt  
# 2) now that we have sbt we can upgrade it to 0.13.1  
RUN wget http://repo.scala-sbt.org/scalasbt/sbt-native-packages/org/scala-
sbt/sbt/0.13.1/sbt.deb  
RUN dpkg -i sbt.deb  
RUN rm -f sbt.deb  
  
# print versions  
RUN java -version  
# scala -version returns code 1 instead of 0 thus || echo '' > /dev/null  
RUN scala -version || echo '' > /dev/null  
# fetches all sbt jars from Maven repo so that your sbt will be ready to be
used when you launch the image  
RUN sbt --version  

