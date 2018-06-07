FROM openjdk:8u131-jdk  
  
RUN addgroup scala && useradd scala -g scala -s /bin/bash -m  
  
ENV SCALA_VERSION 2.11.7  
ENV SBT_VERSION 0.13.15  
RUN mkdir /scala  
COPY sbt /scala  
  
RUN curl -SLf -o /scala/sbt-launch.jar https://repo.typesafe.com/typesafe/ivy-
releases/org.scala-sbt/sbt-launch/$SBT_VERSION/sbt-launch.jar  
  
RUN mkdir ~/tmp  
RUN curl -SLf
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz \  
| tar xfz - -C ~/tmp \  
&& cp -r ~/tmp/scala-$SCALA_VERSION/. /scala \  
&& rm -rf ~/tmp  
  
RUN chown scala:scala -R /scala/*  
RUN chmod +x /scala/sbt  
USER scala  
ENV PATH /scala:$PATH  
  
RUN sbt  
  

