#  
# Scala,sbt (with common plugins) and JavaFX Dockerfile  
#  
# https://bitbucket.org/OPAL-Project/dockerforopal  
#  
# Pull base image  
FROM openjdk:8  
ENV SCALA_VERSION 2.12.6  
ENV SBT_VERSION 1.1.5  
# Scala expects this file  
RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release  
  
# Install Scala  
## Piping curl directly in tar  
RUN \  
curl -fsL
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C /root/ && \  
echo >> /root/.bashrc && \  
echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc  
  
# Install sbt  
RUN \  
curl -L -o sbt-$SBT_VERSION.deb
http://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
apt-get update && \  
apt-get install sbt  
  
# Install openjfx  
RUN \  
apt-get -y install openjfx  
  
# Install the template project using the latest release  
WORKDIR /root  
WORKDIR MyOPALProject  
RUN \  
git clone \--depth 1 https://bitbucket.org/OPAL-Project/myopalproject.git . &&
\  
sbt run  
  
# Install the most current snapshot version (at the time of building this
image) found in the develop branch  
WORKDIR /root  
WORKDIR OPAL  
RUN \  
git clone -b develop --depth 1 https://delors@bitbucket.org/delors/opal.git .
&& \  
sbt compile  

