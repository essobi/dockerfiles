FROM debian:8.0  
MAINTAINER andystanton  
ENV LANG C.UTF-8  
ENV SCALA_VERSION 2.11.6  
RUN apt-get update -qq -y && \  
apt-get install -y patch wget openjdk-7-jre-headless && \  
wget
http://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz
&& \  
mkdir -p /opt/scala && \  
tar -xvf scala-${SCALA_VERSION}.tgz -C /opt/scala && \  
rm scala-${SCALA_VERSION}.tgz && \  
ln -s /opt/scala/scala-${SCALA_VERSION} /opt/scala/current && \  
apt-get remove -y wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
ENV PATH /opt/scala/current/bin:$PATH  
ADD image-common /tmp/dexec/image-common  
VOLUME /tmp/dexec/build  
ENTRYPOINT ["/tmp/dexec/image-common/dexec-script.sh", "scala"]  

