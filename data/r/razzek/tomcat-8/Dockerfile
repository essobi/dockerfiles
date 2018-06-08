FROM tomcat:8.0-jre8  
  
RUN LOG4J_VER=1.2.17 \  
&& curl -SLfs
https://repo1.maven.org/maven2/log4j/log4j/${LOG4J_VER}/log4j-${LOG4J_VER}.jar
> $CATALINA_HOME/lib/log4j-${LOG4J_VER}.jar \  
&& echo "04a41f0a068986f0f73485cf507c0f40
$CATALINA_HOME/lib/log4j-${LOG4J_VER}.jar" | md5sum -c \  
&& rm "$CATALINA_HOME/conf/logging.properties"  
  
RUN SLF4J_VER=1.7.25 \  
&& curl -SLfs
https://repo1.maven.org/maven2/org/slf4j/slf4j-api/${SLF4J_VER}/slf4j-api-${SLF4J_VER}.jar
> $CATALINA_HOME/lib/slf4j-api-${SLF4J_VER}.jar \  
&& echo "caafe376afb7086dcbee79f780394ca3
$CATALINA_HOME/lib/slf4j-api-${SLF4J_VER}.jar" | md5sum -c \  
&& curl -SLfs
https://repo1.maven.org/maven2/org/slf4j/slf4j-log4j12/${SLF4J_VER}/slf4j-log4j12-${SLF4J_VER}.jar
> $CATALINA_HOME/lib/slf4j-log4j12-${SLF4J_VER}.jar \  
&& echo "7f16ba3b1ab6a781c3f6887eae7b608d
$CATALINA_HOME/lib/slf4j-log4j12-${SLF4J_VER}.jar" | md5sum -c  
  
RUN curl -SLfs http://www-
eu.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/extras/tomcat-juli-
adapters.jar > $CATALINA_HOME/lib/tomcat-juli-adapters.jar \  
&& echo "57e3435ae1e0c3a3a1c7b75ee62a0b8b $CATALINA_HOME/lib/tomcat-juli-
adapters.jar" | md5sum -c \  
&& curl -SLfs http://www-
eu.apache.org/dist/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/extras/tomcat-
juli.jar > $CATALINA_HOME/bin/tomcat-juli.jar \  
&& echo "842ec97d998202d1d8a05e492ca55578 $CATALINA_HOME/bin/tomcat-juli.jar"
| md5sum -c  
  
RUN curl -SLfs https://repo1.maven.org/maven2/mysql/mysql-connector-
java/6.0.6/mysql-connector-java-6.0.6.jar > $CATALINA_HOME/lib/mysql-
connector-java-6.0.6.jar \  
&& echo "2420a107fd55bd46541844a0f43d4cdf $CATALINA_HOME/lib/mysql-connector-
java-6.0.6.jar" | md5sum -c  
  
COPY log4j.properties $CATALINA_HOME/lib/

