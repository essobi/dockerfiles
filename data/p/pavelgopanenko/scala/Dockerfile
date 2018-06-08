FROM pavelgopanenko/java:oracle-8u66-b17  
  
ENV SCALA_HOME=/usr/share/scala \  
SCALA_VERSION=2.11.8 \  
SBT_HOME=/usr/local/sbt \  
SBT_VERSION=0.13.8  
# Scala  
RUN apk add --update bash \  
&& cd /tmp \  
&& wget
"http://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz"
\  
&& tar xzf "scala-${SCALA_VERSION}.tgz" \  
&& mkdir "${SCALA_HOME}" \  
&& rm "/tmp/scala-${SCALA_VERSION}/bin/"*.bat \  
&& mv "/tmp/scala-${SCALA_VERSION}/bin" "/tmp/scala-${SCALA_VERSION}/lib"
"${SCALA_HOME}" \  
&& ln -s "${SCALA_HOME}/bin/"* /usr/bin/ \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
# SBT  
RUN curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/${SBT_VERSION}/sbt-${SBT_VERSION}.tgz" | gunzip | tar -x -C
/usr/local \  
&& ln -s /usr/local/sbt/bin/* /usr/bin/ \  
&& echo -ne "- with sbt ${SBT_VERSION}\n" >> /root/.built  
  
ENTRYPOINT []  
CMD [ "scala", "-version" ]  

