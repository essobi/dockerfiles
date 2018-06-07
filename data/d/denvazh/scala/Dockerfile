#  
# Scala with sbt based on lightweight java docker image  
#  
# Manual sbt install is based on:  
# http://www.scala-sbt.org/0.13/tutorial/Manual-Installation.html  
FROM denvazh/java:openjdk8-jdk  
  
MAINTAINER Denis Vazhenin <denis.vazhenin@me.com>  
  
# Versions  
ENV SCALA_VERSION 2.11.7  
ENV SBT_VERSION 0.13.11  
# Install scala and sbt  
RUN \  
echo 'Installing scala...' && \  
wget "http://www.scala-lang.org/files/archive/scala-$SCALA_VERSION.tgz" && \  
tar xzf scala-$SCALA_VERSION.tgz -C /tmp/ && \  
mv /tmp/scala-$SCALA_VERSION/* /usr/local/ && \  
rm -rf scala-$SCALA_VERSION.tgz && \  
echo 'Installing sbt...' && \  
wget "https://dl.bintray.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/$SBT_VERSION/sbt-launch.jar" -P /usr/local/bin/ && \  
echo '#!/bin/bash' > /usr/local/bin/sbt && \  
echo 'SBT_OPTS="-Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled"' >>
/usr/local/bin/sbt && \  
echo 'java $SBT_OPTS -jar `dirname $0`/sbt-launch.jar "$@"' >>
/usr/local/bin/sbt && \  
chmod u+x /usr/local/bin/sbt && \  
echo 'Fetching all sbt related dependencies...' && \  
mkdir -p /tmp/sbt-dummy && \  
echo 'name := "DummyProject"' > /tmp/sbt-dummy/build.sbt && \  
echo 'version := "1.0"' >> /tmp/sbt-dummy/build.sbt && \  
echo "scalaVersion := \"$SCALA_VERSION\"" >> /tmp/sbt-dummy/build.sbt && \  
mkdir -p /tmp/sbt-dummy/src/main/scala && \  
echo 'object Main { def main(args: Array[String]) = println("Dummy") }' >
/tmp/sbt-dummy/src/main/scala/Main.scala && \  
cd /tmp/sbt-dummy && sbt run && \  
rm -rf /tmp/*  
  
# Set scala home for current installation  
ENV SCALA_HOME /usr/local  
  
# Run scala as default command  
CMD ["scala"]  

