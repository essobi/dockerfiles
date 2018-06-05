FROM frolvlad/alpine-oraclejdk8  
  
COPY sbt /usr/local/bin/  
  
RUN \  
apk -U add bash && \  
wget -P /usr/local/bin http://repo.typesafe.com/typesafe/ivy-
releases/org.scala-sbt/sbt-launch/0.13.9/sbt-launch.jar && \  
chmod u+x usr/local/bin/sbt && \  
sync && \  
sbt sbtVersion  
  
CMD ["/bin/bash"]  

