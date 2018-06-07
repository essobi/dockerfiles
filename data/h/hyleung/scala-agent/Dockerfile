FROM hyleung/jenkins-agent  
MAINTAINER H.Y. Leung <hy.leung@gmail.com>  
  
RUN apt-get install -y curl  
RUN curl -L http://dl.bintray.com/sbt/debian/sbt-0.13.5.deb -o /tmp/sbt.deb  
  
RUN dpkg -i /tmp/sbt.deb  
  
RUN curl -L
http://downloads.typesafe.com/scala/2.11.1/scala-2.11.1.deb?_ga=1.13852663.1191924784.1348294022
-o /tmp/scala.deb  
  
RUN dpkg -i /tmp/scala.deb  

