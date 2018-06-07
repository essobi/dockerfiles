FROM fedora:28  
#Derived from official TeamCity image  
LABEL modified "Alexis Jeandet <alexis.jeandet@member.fsf.org>"  
  
RUN dnf install -y java-1.8.0-openjdk mercurial git make cmake meson tar gzip
unzip xorg-x11-server-Xvfb  
  
VOLUME /data/teamcity_agent/conf  
ENV CONFIG_FILE=/data/teamcity_agent/conf/buildAgent.properties \  
TEAMCITY_AGENT_DIST=/opt/buildagent  
  
RUN mkdir $TEAMCITY_AGENT_DIST  
  
ADD https://teamcity.jetbrains.com/update/buildAgent.zip $TEAMCITY_AGENT_DIST/  
RUN unzip $TEAMCITY_AGENT_DIST/buildAgent.zip -d $TEAMCITY_AGENT_DIST/  
  
LABEL dockerImage.teamcity.version="latest" \  
dockerImage.teamcity.buildNumber="latest"  
  
COPY run-agent.sh /run-agent.sh  
COPY run-services.sh /run-services.sh  
  
RUN useradd -m buildagent && \  
chmod +x /run-agent.sh /run-services.sh && \  
rm $TEAMCITY_AGENT_DIST/buildAgent.zip && \  
sync  
#add line return for derived images  
RUN echo " " >> /opt/buildagent/conf/buildAgent.dist.properties && \  
echo "system.distrib=fedora" >>
/opt/buildagent/conf/buildAgent.dist.properties && \  
echo "system.agent_name=minimal-agent" >>
/opt/buildagent/conf/buildAgent.dist.properties && \  
echo "system.agent_repo=https://github.com/jeandet/teamcity-docker-minimal-
agent" >> /opt/buildagent/conf/buildAgent.dist.properties  
  
CMD ["/run-services.sh"]  
  
EXPOSE 9090  

