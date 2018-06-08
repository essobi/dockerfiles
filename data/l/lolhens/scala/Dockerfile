FROM lolhens/baseimage-openjre:latest  
MAINTAINER LolHens <pierrekisters@gmail.com>  
  
  
ENV SCALA_VERSION 2.12.6  
ENV SCALA_NAME scala-$SCALA_VERSION  
ENV SCALA_FILE $SCALA_NAME.tgz  
ENV SCALA_URL http://downloads.lightbend.com/scala/$SCALA_VERSION/$SCALA_FILE  
  
  
RUN cd "/tmp" \  
&& curl -LO $SCALA_URL \  
&& tar -zxf $SCALA_FILE \  
&& mv $SCALA_NAME "/usr/share/scala/" \  
&& ln -s /usr/share/scala/bin/scala /usr/bin/scala \  
&& ln -s /usr/share/scala/bin/scalac /usr/bin/scalac \  
&& ln -s /usr/share/scala/bin/fsc /usr/bin/fsc \  
&& ln -s /usr/share/scala/bin/scaladoc /usr/bin/scaladoc \  
&& ln -s /usr/share/scala/bin/scalap /usr/bin/scalap \  
&& cleanimage  
  
  
CMD scala  

