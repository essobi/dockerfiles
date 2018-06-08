#  
# Scala and sbt Dockerfile  
#  
# https://github.com/spikerlabs/scala-sbt (based on
https://github.com/hseeberger/scala-sbt)  
#  
# Pull base image  
FROM openjdk:11-jdk-slim  
  
ARG SCALA_VERSION  
ARG SBT_VERSION  
  
ENV SCALA_VERSION ${SCALA_VERSION:-2.12.6}  
ENV SBT_VERSION ${SBT_VERSION:-1.1.6}  
  
RUN \  
echo "$SCALA_VERSION $SBT_VERSION" && \  
apt-get update -y && \  
apt-get install -y bash \  
curl \  
openssh-client \  
apt-transport-https \  
ca-certificates \  
curl \  
gnupg2 \  
software-properties-common \  
&& curl -fsL
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C /usr/local && \  
ln -s /usr/local/scala-$SCALA_VERSION/bin/* /usr/local/bin/ && \  
scala -version && \  
scalac -version  
  
RUN \  
curl -fsSL get.docker.com -o get-docker.sh && \  
sh get-docker.sh  
  
RUN \  
systemctl enable docker  
  
RUN \  
curl -fsL
https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz
| tar xfz - -C /usr/local && \  
$(mv /usr/local/sbt-launcher-packaging-$SBT_VERSION /usr/local/sbt || true) \  
ln -s /usr/local/sbt/bin/* /usr/local/bin/ && \  
sbt sbt-version || sbt sbtVersion || true  
  
ENTRYPOINT ["/etc/init.d/docker","start"]  

