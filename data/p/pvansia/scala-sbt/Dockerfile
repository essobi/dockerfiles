FROM openjdk:8-alpine  
  
MAINTAINER Pinkal Vansia <p.vansia@gmail.com>  
  
ENV SBT_VERSION 0.13.13  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
# Install sbt  
RUN apk add --update curl bash && \  
curl -L "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local && \  
mv /usr/local/sbt-launcher-packaging-0.13.13 ${SBT_HOME} && \  
echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built  
  
WORKDIR /app  
  
# Web Port  
EXPOSE 9000  
# Debug Port  
EXPOSE 9999

