FROM vtor/dev-jdk8:latest  
  
MAINTAINER vt <vardants@gmail.com>  
  
ENV SCALA_VERSION 2.12.2  
ENV SBT_VERSION 0.13.15  
RUN apt-get update && apt-get install curl  
  
# Install Scala  
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
  
# Install ammonite  
RUN mkdir ~/.ammonite && curl -Ls -o ~/.ammonite/predef.scala
https://git.io/vro0a  
RUN curl -Ls -o /bin/amm https://git.io/vro0u && chmod +x /bin/amm  
  
CMD ["bash"]

