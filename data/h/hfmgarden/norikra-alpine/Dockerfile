FROM jruby:9.1-alpine  
MAINTAINER OKUMURA Takahiro <hfm.garden@gmail.com>  
  
ENV NORIKRA_VERSION=1.5.1 JOLOKIA_VERSION=1.3.5  
RUN mkdir /opt/jolokia \  
&& wget -O /opt/jolokia/jolokia-jvm-agent.jar
http://central.maven.org/maven2/org/jolokia/jolokia-
jvm/${JOLOKIA_VERSION}/jolokia-jvm-${JOLOKIA_VERSION}-agent.jar \  
&& gem install norikra --no-document -v $NORIKRA_VERSION  
  
EXPOSE 26571 26578 8778  
CMD ["norikra", "start", "-javaagent:/opt/jolokia/jolokia-jvm-
agent.jar=port=8778,host=0.0.0.0,discoveryEnabled=false", "--stats",
"/var/tmp/norikra/stats.json", "-l", "/var/tmp/norikra"]  

