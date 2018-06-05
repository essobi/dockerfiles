FROM zhaowh/centos-java  
MAINTAINER Zhao Weihong  
  
RUN cd /opt && \  
wget http://downloads.typesafe.com/typesafe-activator/1.2.2/typesafe-
activator-1.2.2.zip && \  
unzip typesafe-activator-1.2.2.zip && \  
rm -f /opt/typesafe-activator-1.2.2.zip && \  
mv /opt/activator-1.2.2 /opt/activator && \  
ln -s /opt/activator/activator /usr/local/bin/activator  
  
RUN cd /opt/activator/repository/org.scala-lang/scala-compiler/2.10.2/ && \  
mkdir jars && cd jars && \  
wget http://repo1.maven.org/maven2/org/scala-lang/scala-compiler/2.10.2/scala-
compiler-2.10.2.jar -O scala-compiler.jar  
  
VOLUME ["/data"]  
WORKDIR /data  
EXPOSE 8888 9000  
CMD ["/opt/activator/activator", "ui", "-Dhttp.address=0.0.0.0",
"-Dorg.slf4j.simpleLogger.defaultLogLevel=trace"]  
  

