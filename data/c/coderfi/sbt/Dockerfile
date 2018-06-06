# Scala and sbt Docker Image on Oracle Java 8  
#  
# URL: https://github.com/coderfi/docker-scala  
#  
# based on:  
# - pulse00/scala  
# - williamyeh/scal  
# - errordeveloper/sbt  
FROM dockerfile/java:oracle-java8  
MAINTAINER Fairiz Azizi <coderfi@gmail.com>  
  
ENV SCALA_VERSION 2.11.6  
ENV SBT_VERSION 0.13.8  
ENV SCALA_TARBALL http://www.scala-
lang.org/files/archive/scala-${SCALA_VERSION}.deb  
ENV SBT_JAR https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/${SBT_VERSION}/sbt-launch.jar  
  
RUN echo "*** install typesafe repo" \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --force-yes wget \  
&& wget http://apt.typesafe.com/repo-deb-build-0002.deb \  
&& dpkg -i repo-deb-build-0002.deb \  
&& apt-get update \  
\  
&& echo "*** install Scala v${SCALA_VERSION}" \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install -y --force-yes libjansi-java \  
&& wget -nv $SCALA_TARBALL \  
&& dpkg -i scala-*.deb \  
\  
&& echo "*** install sbt v${SBT_VERSION}" \  
&& wget -nv -P /usr/local/bin/ ${SBT_JAR} \  
\  
&& echo "*** cleaning up" \  
&& rm -f *.deb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY sbt /usr/local/bin/  
  
ENTRYPOINT ["/usr/local/bin/sbt"]

