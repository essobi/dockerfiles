FROM sergeyzh/tomcat7:jdk7  
  
MAINTAINER Sergey Zhukov, sergey@jetbrains.com  
  
ENV LOG4J_VER 1.2.17  
ENV LOG4J_BIN log4j-${LOG4J_VER}.tar.gz  
  
# Download appropriate juli libs  
RUN URL=`curl https://tomcat.apache.org/download-70.cgi | \  
grep Browse | grep -v www.apache.org | sed
"s#.*href=\"\\(.*${TOMCAT_VER}\\)\".*#\1#"` && \  
wget -O /home/tomcat/apache-tomcat-current/bin/tomcat-juli.jar
${URL}/bin/extras/tomcat-juli.jar && \  
wget -O /home/tomcat/apache-tomcat-current/lib/tomcat-juli-adapters.jar
${URL}/bin/extras/tomcat-juli-adapters.jar  
  
RUN wget -O /home/tomcat/${LOG4J_BIN} http://apache-
mirror.rbc.ru/pub/apache/logging/log4j/${LOG4J_VER}/${LOG4J_BIN} && \  
cd /home/tomcat/ && tar -xzf ${LOG4J_BIN} && mv apache-
log4j-${LOG4J_VER}/log4j-${LOG4J_VER}.jar /home/tomcat/apache-tomcat-
current/lib/ && \  
rm -rf apache-log4j-${LOG4J_VER} ${LOG4J_BIN}  
  
ADD tomcat-log4j.xml /home/tomcat/apache-tomcat-current/conf/  
ADD log4j.dtd /home/tomcat/apache-tomcat-current/conf/  
  
# Apply additional transformations to children images  
ONBUILD ADD wrapper /home/tomcat/wrapper/  
ONBUILD ADD xslt /home/tomcat/xslt/  
ONBUILD ADD cacerts /home/tomcat/cacerts/  
ONBUILD RUN bash -c ". /apply.sh"  
  

