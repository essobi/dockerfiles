FROM taig/java:1.0.7  
MAINTAINER Niklas Klein "mail@taig.io"  
ENV SBT 0.13.13  
ENV SCALA 2.12.1  
WORKDIR /root/  
  
RUN wget \  
https://raw.githubusercontent.com/paulp/sbt-extras/master/sbt \  
-O /bin/sbt  
RUN chmod +x /bin/sbt  
  
RUN mkdir -p ./cache/project/  
RUN mkdir -p ./cache/src/main/scala/  
RUN echo "sbt.version=${SBT}" > ./cache/project/build.properties  
RUN echo "scalaVersion := \"${SCALA}\"" > ./cache/build.sbt  
RUN echo "crossScalaVersions := Seq(\"2.11.8\", \"2.12.0\", \"$SCALA\")" >>
./cache/build.sbt  
RUN echo "object Dummy" > ./cache/src/main/scala/Dummy.scala  
RUN cd ./cache/ && sbt +compile  
RUN rm -r ./cache/

