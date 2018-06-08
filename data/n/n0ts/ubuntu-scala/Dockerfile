FROM n0ts/ubuntu-java  
  
MAINTAINER Naoya Nakazawa <naoya.n@gmail.com>  
  
# https://github.com/scala/scala/releases  
##ENV SCALA_VER 2.11.11  
# https://github.com/sbt/sbt/releases  
##ENV SBT_VER 0.13.13  
  
RUN set -x \  
# install scala  
&& SCALA_VER=$(curl -s -o /dev/null -I -w "%{redirect_url}\n"
https://github.com/scala/scala/releases/latest | grep -oP
"[0-9]+.[0-9]+.[0-9]+$") \  
&& curl -L -o /opt/scala-$SCALA_VER.deb \  
https://www.scala-lang.org/files/archive/scala-$SCALA_VER.deb \  
&& dpkg -i /opt/scala-$SCALA_VER.deb \  
&& rm -f /opt/scala-$SCALA_VER.deb \  
  
# install sbt  
&& SBT_VER=$(curl -s -o /dev/null -I -w "%{redirect_url}\n"
https://github.com/sbt/sbt/releases/latest | grep -oP "[0-9]+.[0-9]+.[0-9]+$")
\  
&& curl -L -o /opt/sbt-$SBT_VER.deb \  
https://dl.bintray.com/sbt/debian/sbt-${SBT_VER}.deb \  
&& dpkg -i /opt/sbt-$SBT_VER.deb \  
&& sbt about  
  
CMD ["/bin/bash"]  

