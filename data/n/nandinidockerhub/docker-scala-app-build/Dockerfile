#  
# Scala and sbt Dockerfile  
#  
# https://github.com/hseeberger/scala-sbt  
#  
# Pull base image  
FROM java:8  
ENV SCALA_VERSION 2.11.8  
ENV SBT_VERSION 0.13.12  
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
apt-get install sbt && \  
sbt sbtVersion  
  
#Install vim  
RUN apt-get update  
RUN apt-get install -y vim  
  
EXPOSE 9000  
EXPOSE 8080  
EXPOSE 27017  
RUN mkdir /app  
WORKDIR /app  
  
RUN git clone https://github.com/nandinicbit1981/ScalaPlayDemo.git  
WORKDIR /app/ScalaPlayDemo  
  
CMD ["sbt", "run"]  

