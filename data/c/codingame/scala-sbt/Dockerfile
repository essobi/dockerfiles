FROM codingame/sbt:0.13.15  
ENV SCALA_VERSION 2.12.2  
ENV SCALA_ARCHIVE http://www.scala-
lang.org/files/archive/scala-${SCALA_VERSION}.tgz  
ENV SCALA_HOME /usr/local/share/scala  
ENV PATH ${PATH}:${SCALA_HOME}/bin  
ENV SBT_OPTS "-Xmx768M -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled
-Xss2M -Duser.timezone=GMT"  
# Install Scala  
RUN mkdir -p "$SCALA_HOME" \  
&& curl -sSL "$SCALA_ARCHIVE" \  
| tar -xzC "$SCALA_HOME" \--strip-components=1  

