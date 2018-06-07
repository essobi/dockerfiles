FROM anapsix/alpine-java:jdk8  
  
ENV SBT_VERSION 0.13.11  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
RUN set -x \  
&& wget "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" \  
&& gunzip sbt-$SBT_VERSION.tgz \  
&& tar -x -C /usr/local -f sbt-$SBT_VERSION.tar \  
&& echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built  
  
WORKDIR /app  

