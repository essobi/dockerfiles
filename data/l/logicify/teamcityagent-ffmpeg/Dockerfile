FROM logicify/ffmpeg:2.7.1  
RUN yum -y update \  
&& yum install -y python-dev python-pip gcc make gcc-c++ \  
&& yum install -y libpng libjpeg ImageMagick GraphicsMagick \  
&& yum clean all  
  
# --------------------------------------------------------------- teamcity-
agent  
ENV TEAMCITY_VERSION 9.0.4  
ENV TEAMCITY_GIT_PATH /usr/bin/git  
ENV AGENT_PORT 9090  
RUN curl -LO
http://download.jetbrains.com/teamcity/TeamCity-$TEAMCITY_VERSION.war \  
&& unzip -qq TeamCity-$TEAMCITY_VERSION.war -d /tmp/teamcity \  
&& unzip -qq /tmp/teamcity/update/buildAgent.zip -d /srv/teamcity-agent  
  
COPY start-agent.sh /srv/  
  
RUN chmod +x /srv/teamcity-agent/bin/*.sh \  
&& chmod +x /srv/*.sh \  
&& mv /srv/teamcity-agent/conf/buildAgent.dist.properties /srv/teamcity-
agent/conf/buildAgent.properties \  
  
&& rm -f TeamCity-$TEAMCITY_VERSION.war \  
&& rm -fR /tmp/* \  
&& chown -R app:app /srv/teamcity-agent  
  
  
# -----------------------------------------------------------------------
nodejs  
ENV NODE_VERSION 0.12.2  
RUN (curl -L
http://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
| gunzip -c | tar x) \  
&& cp -R node-v${NODE_VERSION}-linux-x64/* /usr/ \  
&& rm -fR node-v${NODE_VERSION}-linux-x64 \  
&& npm update -g \  
&& npm install -g node-gyp grunt grunt-cli karma-cli bower aglio  
  
# ------------------------------------------------------------------------
maven  
ENV MAVEN_VERSION 3.3.3  
RUN (curl -L
http://www.us.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | gunzip -c | tar x) \  
&& mv apache-maven-$MAVEN_VERSION /opt/apache-maven  
  
ENV M2_HOME /opt/apache-maven  
ENV MAVEN_OPTS -Xmx512m -Xss256k -XX:+UseCompressedOops  
  
# ------------------------------------------------------------------------
docker  
RUN yum install -y docker-client python-devel gcc && yum clean all \  
&& pip install docker-compose maestro-ng  
ENV DOCKER_AVAILABLE=1  
# ------------------------------------------------------------------------  
EXPOSE ${AGENT_PORT}  
VOLUME /srv/teamcity-agent/conf  
USER app  
  
CMD ["/srv/start-agent.sh"]  

