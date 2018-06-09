FROM java:8-jdk  
  
MAINTAINER Antonio Alonso Dominguez "alonso@codenibbles.com"  
  
ENV TEAMCITY_VERSION 9.1.7  
ENV TEAMCITY_AGENT_HOME /opt/lib/teamcity-agent  
  
RUN mkdir -p /etc/teamcity-agent  
  
COPY conf/* /etc/teamcity-agent/  
  
RUN mkdir -p /opt/lib && \  
wget -nv http://download.jetbrains.com/teamcity/TeamCity-$TEAMCITY_VERSION.war
-O /tmp/TeamCity-$TEAMCITY_VERSION.war && \  
unzip -qq /tmp/TeamCity-$TEAMCITY_VERSION.war -d /tmp/teamcity && \  
unzip -qq /tmp/teamcity/update/buildAgent.zip -d $TEAMCITY_AGENT_HOME && \  
chmod +x $TEAMCITY_AGENT_HOME/bin/*.sh && \  
rm -f $TEAMCITY_AGENT_HOME/conf/buildAgent.properties && \  
ln -s /etc/teamcity-agent/buildAgent.properties
$TEAMCITY_AGENT_HOME/conf/buildAgent.properties && \  
rm -fR /tmp/*  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
EXPOSE 9090  
  
VOLUME [ "/etc/teamcity-agent" ]  
  
WORKDIR /opt/lib/teamcity-agent  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

