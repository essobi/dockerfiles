FROM zephyre/docker-java:latest  
MAINTAINER Zephyre <haizi.zh@gmail.com>  
  
ENV SBT_VERSION 0.13.8  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
# Install sbt  
RUN curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local && \  
echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built  
  
WORKDIR /app  
  
ENTRYPOINT ["/usr/local/sbt/bin/sbt"]  

