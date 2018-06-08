# Main reference: https://gist.github.com/bigsnarfdude/b2eb1cabfdaf7e62a8fc  
# For building this image, See https://github.com/GELOG/docker-ubuntu-java  
FROM gelog/java:openjdk7  
  
  
# Environment variables  
ENV SBT_VERSION 0.13.6  
ENV SBT_HOME /usr/local/sbt  
ENV SCALA_VERSION 2.11.4  
ENV SCALA_HOME /usr/local/scala  
ENV PATH $SCALA_HOME/bin:$SBT_HOME/bin:$PATH  
  
  
# Installing Scala from source  
RUN wget http://www.scala-lang.org/files/archive/scala-$SCALA_VERSION.tgz && \  
tar -xzf /scala-$SCALA_VERSION.tgz -C /usr/local/ && \  
ln -s /usr/local/scala-$SCALA_VERSION $SCALA_HOME && \  
rm scala-$SCALA_VERSION.tgz  
  
# Installing SBT from source  
RUN wget https://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz && \  
tar -xzf sbt-$SBT_VERSION.tgz -C /usr/local/ && \  
rm sbt-$SBT_VERSION.tgz && \  
echo "Show SBT version" && \  
sbt about  
# FIXME: running "sbt about" seems to re-download Scala. TODO: find out what
is happening.  
# e.g. do we need to install Scala in the first place ??  
# Default action: starts a Scala shell  
CMD ["scala"]  
  

