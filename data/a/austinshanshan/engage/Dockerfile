FROM openjdk:8  
MAINTAINER SHAN SHAN <sshan@cognitivescale.com>  
  
ENV SCALA_VERSION 2.12.1  
ENV SBT_VERSION 0.13.13  
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
apt-get install sbt && \  
sbt sbtVersion  
  
#RUN mkdir -p /root/.ssh  
#ADD id_rsa /root/.ssh/id_rsa  
#RUN chmod 700 /root/.ssh/id_rsa  
#RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config  
RUN mkdir /engage  
WORKDIR /engage  
RUN git clone git@github.com:sshanamplify/engage-testing.git /engage  
ENV SCALA_ENV=qa  
  
RUN ls -lrt  
  
CMD ["sbt "testOnly: EngageProfileLoad""]  

