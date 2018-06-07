FROM duffqiu/dockerjdk7:latest  
MAINTAINER duffqiu@gmail.com  
  
RUN yum -y update  
RUN yum install -y wget  
  
# install mesos from mesosphere  
ENV SCALA_VERSION 2.11.5  
ENV SBT_VERSION 0.13.8  
ENV SCALA_HOME /usr/share/scala  
  
# Download and install the required version of Scala  
RUN yum install -y wget \  
&& wget
"http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.rpm"
\  
&& wget "https://repo.typesafe.com/typesafe/ivy-releases/org.scala-sbt/sbt-
launch/$SBT_VERSION/sbt-launch.jar" -O /usr/local/bin/sbt-launch.jar \  
&& yum install -y "scala-$SCALA_VERSION.rpm" sbt \  
&& yum clean all \  
&& rm -rf "scala-$SCALA_VERSION.rpm"  
  
# Copy the SBT shell script into the image  
COPY sbt /usr/local/bin/  
RUN chmod u+x /usr/local/bin/sbt  
  
# Force SBT to download dependancies and then exit  
RUN sbt exit  
  
# If running this image directly, we most likely want the scala REPL  
ENTRYPOINT [ "scala" ]  

