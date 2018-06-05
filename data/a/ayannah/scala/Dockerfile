FROM java:7  
MAINTAINER John Paul Alcala, jpalcala@ayannah.com  
  
ENV SCALA_VERSION 2.10.5  
ENV SCALA_HOME /usr/local/scala  
ENV SBT_HOME /usr/local/sbt  
ENV SBT_OPTS -Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled
-XX:MaxPermSize=256M  
  
RUN mkdir -p $SCALA_HOME && \  
curl -SL
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xzf - -C $SCALA_HOME \--strip-components=1 && \  
mkdir -p $SBT_HOME && \  
curl -SL https://dl.bintray.com/sbt/native-packages/sbt/0.13.8/sbt-0.13.8.tgz
| tar xzf - -C $SBT_HOME \--strip-components=1 && \  
ln -s \  
$SCALA_HOME/bin/fsc \  
$SCALA_HOME/bin/scala \  
$SCALA_HOME/bin/scalac \  
$SCALA_HOME/bin/scaladoc \  
$SCALA_HOME/bin/scalap \  
$SBT_HOME/bin/sbt \  
/usr/local/bin && \  
sbt -batch  
  
CMD ["sbt"]  

