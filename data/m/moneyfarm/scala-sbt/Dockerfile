# Scala and sbt Dockerfile  
FROM openjdk:8u141-jdk  
  
ENV SCALA_VERSION 2.12.3  
ENV SBT_VERSION 1.0.2  
# Scala expects this file  
RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release  
  
# Install Scala  
RUN \  
curl -fsL
https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C /root/ && \  
echo >> /root/.bashrc && \  
echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc  
  
# Install sbt  
RUN \  
curl -L -o sbt-$SBT_VERSION.deb
https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
apt-get update && \  
apt-get install sbt && \  
sbt sbtVersion  
  
# Add jenkins user  
RUN \  
adduser --home /var/jenkins_home --disabled-password --uid 1000 jenkins  
  
# Add Wkhtmltopdf  
RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz && \  
tar xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz -C /opt && \  
rm wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
  
ENV PATH=$PATH:/opt/wkhtmltox/bin  
  
# Define working directory  
WORKDIR /root%  

