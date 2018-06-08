########################################################  
# Dockerfile for image with Scala, SBT and some common dependencies  
#  
# https://github.com/kpmeen/docker-scala-sbt  
########################################################  
FROM openjdk:8  
  
ENV SCALA_VERSION 2.11.11  
ENV SBT_VERSION 0.13.16  
  
# Install locales package  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
locales  
  
# Set locale to be en_US.UTF-8  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
  
# Set the LANG environment  
ENV LANG en_US.UTF-8  
ENV COURSIER_CACHE="/root/cache/coursier"  
  
# Install Scala  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0C49F3730359A14518585931BC711F9BA15703C6 && \  
curl -fsL
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C /root/ && \  
echo >> /root/.bashrc && \  
echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc && \  
apt-get update && \  
apt-get -y install apt-transport-https ca-certificates software-properties-
common  
  
# Install sbt and docker-engine  
RUN \  
curl -L -o sbt-$SBT_VERSION.deb
http://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
curl -fsSL https://yum.dockerproject.org/gpg | apt-key add - && \  
add-apt-repository "deb https://apt.dockerproject.org/repo/
debian-$(lsb_release -cs) main" && \  
apt-get update && \  
apt-get -y install docker-engine  
  
# Set up a dummy SBT project  
WORKDIR /play-scala  
COPY ./play-scala /play-scala  
COPY ./sbtopts /etc/sbt/sbtopts  
  
# Prefetch dependencies  
RUN \  
ls && \  
sbt scalafmt test && \  
rm -rf *  
  
# Define working directory  
WORKDIR /root  

