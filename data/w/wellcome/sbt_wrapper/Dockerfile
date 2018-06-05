FROM openjdk:8-alpine  
  
LABEL maintainer "Wellcome <wellcomedigitalplatform@wellcome.ac.uk>"  
LABEL description "A Docker image used for building sbt projects in the
Wellcome Digital Platform"  
  
RUN apk add --update bash curl docker py-pip  
RUN pip install docker-compose  
  
ENV SBT_VERSION 1.1.1  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
RUN curl -L
"https://github.com/sbt/sbt/releases/download/v${SBT_VERSION}/sbt-${SBT_VERSION}.tgz"
| gunzip | tar -x -C /usr/local  
  
VOLUME /repo  
WORKDIR /repo  
  
# We were seeing occasional stack overflow errors since upgrading to scala
2.12  
# This is to increase the default thread stack size so that doesn't happen  
ENTRYPOINT ["/usr/local/sbt/bin/sbt", "-J-Xss2M"]  

