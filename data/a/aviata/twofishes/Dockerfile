FROM library/java:openjdk-7-jdk  
MAINTAINER Dale-Kurt Murray "dalekurt.murray@gmail.com"  
RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get install -y -q
wget unzip \  
&& mkdir /twofishes  
RUN wget http://twofishes.net/binaries/server-assembly-0.84.9.jar -P
/twofishes \  
&& wget http://twofishes.net/indexes/revgeo/2015-03-05.zip -P /twofishes \  
&& unzip /twofishes/2015-03-05.zip -d /twofishes \  
&& rm /twofishes/2015-03-05.zip  
  
VOLUME /twofishes  
  
EXPOSE 8080 8081 8082 8083  
CMD java -Xmx$JVM_MAX_MEM -jar /twofishes/server-assembly-0.84.9.jar
--hfile_basepath /twofishes/2015-03-05-20-05-30.753698  

