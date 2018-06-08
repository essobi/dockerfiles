#  
# Scala base DockerfileOracle Java 8 Dockerfile  
# https://github.com/rorygraves/scalabase/  
#  
# Pull base image from phusion  
FROM phusion/baseimage  
  
MAINTAINER Rory Graves, rory.graves@fieldmark.co.uk  
  
# Install git and a few other useful gits  
RUN\  
echo "installing curl git locals ca-certifcates" &&\  
apt-get update && \  
apt-get install -y curl git locales ca-certificates &&\  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen &&\  
locale-gen &&\  
apt-get clean  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN \  
java -version  
  
################################################  
# SBT (and by implication, Scala)  
ADD https://raw.githubusercontent.com/paulp/sbt-extras/master/sbt /usr/bin/sbt  
RUN chmod a+rx /usr/bin/sbt  
RUN\  
mkdir /tmp/sbt &&\  
cd /tmp/sbt &&\  
mkdir -p project src/main/scala &&\  
touch src/main/scala/scratch.scala &&\  
echo "sbt.version=0.13.9" > project/build.properties &&\  
sbt ++2.11.7 clean updateClassifiers compile &&\  
rm -rf /tmp/sbt  
  
# Ensime and deps  
RUN\  
cd /root &&\  
git clone https://github.com/ensime/ensime-server.git &&\  
cd ensime-server &&\  
git reset --hard origin/master &&\  
git clean -xfd &&\  
sbt gen-ensime &&\  
rm -rf /root/ensime-server  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  

