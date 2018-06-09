FROM openjdk:8-jdk  
  
ENV SCALA_VERSION 2.12.6  
ENV NODE_VERSION 10.0.0  
ENV SBT_VERSION 1.1.4  
LABEL maintainer="evan@swanaudio.com"  
  
RUN curl -SLO
https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz \  
&& tar -xzf "scala-$SCALA_VERSION.tgz" -C /usr/local \--strip-components=1 \  
&& rm "scala-$SCALA_VERSION.tgz"  
  
# Install sbt  
RUN curl -SLO
https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz
\  
&& tar -xzf "sbt-$SBT_VERSION.tgz" -C /usr/local \--strip-components=1 \  
&& rm "sbt-$SBT_VERSION.tgz" \  
&& sbt -version  
  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache verify  
  
ENTRYPOINT ["sbt"]  

