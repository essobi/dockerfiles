FROM tedneward/java  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
# Get Scala  
#  
ENV SCALA_VER=2.12.3  
RUN wget -O-
"http://downloads.lightbend.com/scala/${SCALA_VER}/scala-${SCALA_VER}.tgz" \  
| tar xzf - -C /usr/local \--strip-components=1  
  
# Get SBT  
#  
ENV SBT_VER 1.0.0  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
RUN curl -sL
"https://github.com/sbt/sbt/releases/download/v${SBT_VER}/sbt-${SBT_VER}.tgz"
\  
| gunzip \  
| tar -x -C /usr/local  
  
RUN sbt help  
  
ENTRYPOINT ["/bin/bash"]  

