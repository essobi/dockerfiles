FROM openjdk:8-jre-alpine  
  
ENV SCALA_HOME /usr/local/share/scala  
ENV PATH $PATH:$SCALA_HOME/bin  
  
ENV SCALA_VERSION 2.12.1  
  
RUN java -version 2>&1 | grep version | sed -e 's/^openjdk version
/JAVA_VERSION=/' > $JAVA_HOME/release  
  
RUN apk add --update wget tar bash && \  
wget --quiet
http://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz
&& \  
tar -xf scala-$SCALA_VERSION.tgz && \  
rm scala-$SCALA_VERSION.tgz && \  
mv scala-$SCALA_VERSION $SCALA_HOME  

