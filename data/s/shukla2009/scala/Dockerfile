FROM isuper/java-oracle:jdk_latest  
  
MAINTAINER Rahul Shukla "rahul.shukla@avaliatech.com"  
ENV SCALA_HOME /usr/local/share/scala  
ENV PATH $PATH:$SCALA_HOME/bin  
  
ENV SCALA_VERSION 2.11.11  
RUN apt-get update && apt-get install wget && \  
wget --quiet
http://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz
&& \  
tar -xf scala-$SCALA_VERSION.tgz && \  
rm scala-$SCALA_VERSION.tgz && \  
mv scala-$SCALA_VERSION $SCALA_HOME  
  
EXPOSE 2552  

