# martinsoto/kafka-manager  
FROM java:8  
MAINTAINER Martin Soto <donsoto@gmail.com>  
  
ENV KM_VERSION=1.3.0.4 \  
KM_REVISION=1b45af100ee302dfe53f31a9c7a041999fe3d83a  
  
RUN echo "deb http://dl.bintray.com/sbt/debian /" >
/etc/apt/sources.list.d/sbt.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
unzip \  
software-properties-common \  
sbt \  
&& cd /tmp \  
&& git clone https://github.com/yahoo/kafka-manager.git \  
&& cd /tmp/kafka-manager \  
&& git checkout ${KM_REVISION} \  
&& echo 'scalacOptions ++= Seq("-Xmax-classfile-name", "200")' >> build.sbt \  
&& cd /tmp/kafka-manager \  
&& sbt clean dist \  
&& unzip -d / ./target/universal/kafka-manager-${KM_VERSION}.zip \  
&& rm -fr /tmp/* /root/.sbt /root/.ivy2 \  
&& DEBIAN_FRONTEND=noninteractive apt-get remove --purge -y \  
unzip \  
software-properties-common \  
sbt \  
&& apt-get autoremove -y \  
&& apt-get clean  
  
ENV KAFKA_MANAGER_HOME=/kafka-manager-${KM_VERSION}  
WORKDIR $KAFKA_MANAGER_HOME  
  
EXPOSE 9000  
ADD start-kafka-manager.sh /usr/bin/  
CMD start-kafka-manager.sh  

