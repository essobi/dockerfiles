FROM hora/recipes-rss-middletier:0.3  
MAINTAINER Teerat Pitakrat  
  
RUN apt-get update && apt-get install -y zip  
  
WORKDIR /opt/recipes-rss/  
#ADD http://search.maven.org/remotecontent?filepath=net/kieker-
monitoring/kieker/1.12/kieker-1.12-aspectj.jar /opt/recipes-
rss/kieker-1.12-aspectj.jar  
ADD
https://oss.sonatype.org/service/local/repositories/snapshots/content/net/kieker-
monitoring/kieker/1.13-SNAPSHOT/kieker-1.13-20170125.034614-257-aspectj.jar
/opt/recipes-rss/kieker-1.13-aspectj.jar  
COPY kieker.monitoring.properties /opt/recipes-
rss/kieker.monitoring.properties  
  
ADD http://central.maven.org/maven2/org/apache/activemq/activemq-
all/5.12.0/activemq-all-5.12.0.jar /opt/recipes-rss/activemq-all-5.12.0.jar  
ADD
http://central.maven.org/maven2/org/slf4j/slf4j-log4j12/1.7.12/slf4j-log4j12-1.7.12.jar
/opt/recipes-rss/slf4j-log4j12-1.7.12.jar  
ADD
http://central.maven.org/maven2/org/apache/logging/log4j/log4j-core/2.4/log4j-core-2.4.jar
/opt/recipes-rss/log4j-core-2.4.jar  
  
COPY aop.xml /opt/recipes-rss/META-INF/aop.xml  
RUN zip -r rss-middletier.jar META-INF  
  
EXPOSE 9191  
CMD ["java", "-javaagent:kieker-1.13-aspectj.jar",
"-Dkieker.monitoring.configuration=kieker.monitoring.properties", "-cp",
"kieker-1.13-aspectj.jar:activemq-
all-5.12.0.jar:slf4j-log4j12-1.7.12.jar:log4j-core-2.4.jar:rss-
middletier.jar", "com.netflix.recipes.rss.server.MiddleTierServer"]  

