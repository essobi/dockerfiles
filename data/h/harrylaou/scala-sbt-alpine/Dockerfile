FROM frolvlad/alpine-scala  
MAINTAINER Harry Laoulakos <harrylaou@gmail.com>  
ENV SCALA_VERSION=2.12.4  
ENV SBT_VERSION=1.0.4  
RUN \  
echo "$SCALA_VERSION $SBT_VERSION" && \  
apk add --no-cache bash curl bc && \  
scala -version && \  
scalac -version && \  
curl -fsL
https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz
| tar xfz - -C /usr/local && \  
$(mv /usr/local/sbt-launcher-packaging-$SBT_VERSION /usr/local/sbt || true) &&
\  
ln -s /usr/local/sbt/bin/* /usr/local/bin/ && \  
apk del curl && \  
sbt sbtVersion  

