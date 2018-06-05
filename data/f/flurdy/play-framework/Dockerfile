FROM flurdy/sbt:1.0.2-alpine  
  
MAINTAINER Ivar Abrahamsen <@flurdy>  
  
RUN mkdir -p /opt/build  
  
WORKDIR /opt/build  
  
ENV SBT_HOME /opt/sbt  
  
RUN \  
sbt new playframework/play-scala-seed.g8 --name=play-base && \  
cd play-base && \  
sbt stage && \  
rm -rf /opt/build  
  

