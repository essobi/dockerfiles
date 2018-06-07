FROM java:8  
ENV SBT_VERSION 0.13.15  
ENV SCALA_VERSION 2.11.8  
ENV COURSIER_VERSION 1.0.0-M15-3  
ENV SCOVERAGE_VERSION 1.4.0  
# scala  
RUN \  
curl -fsL
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C /root/ && \  
echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc  
  
# sbt  
RUN \  
curl -L -o sbt-$SBT_VERSION.deb
http://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
apt-get update && \  
apt-get install sbt  
  
# ivy2 setup  
RUN \  
mkdir -p /root/.sbt/${SBT_VERSION%.*}/plugins && \  
echo 'addSbtPlugin("io.get-coursier" % "sbt-coursier" %
"'$COURSIER_VERSION'")' >> /root/.sbt/${SBT_VERSION%.*}/plugins/plugins.sbt &&
\  
echo 'addSbtPlugin("org.scoverage" % "sbt-scoverage" %
"'$SCOVERAGE_VERSION'")' >> /root/.sbt/${SBT_VERSION%.*}/plugins/plugins.sbt
&& \  
mkdir -p project && \  
echo 'sbt.version='$SBT_VERSION > project/build.properties && \  
echo 'scalaVersion := "'$SCALA_VERSION'"' > build.sbt && \  
echo 'object Test extends App { println("hello") }' > Test.scala && \  
sbt run && \  
rm -rf project build.sbt target Test.scala  
  
WORKDIR /root  
  

