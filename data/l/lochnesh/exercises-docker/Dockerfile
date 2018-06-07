FROM elixir:1.6.1  
  
MAINTAINER Skyler Nesheim  
  
COPY sbt-project /sbt-project  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64  
  
RUN apt-get update && \  
apt-get install apt-transport-https && \  
echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list && \  
apt-key adv \--keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 && \  
echo 'deb http://http.debian.net/debian jessie-backports main' >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y openjdk-8-jdk="8u131-b11-1~bpo8+1" ca-certificates-
java="20161107~bpo8+1" && \  
apt-get install -y sbt && \  
apt-get install -y ruby-full && \  
apt-get install -y bc && \  
gem install bundler && \  
cd /sbt-project && \  
sbt compile  

