FROM logicify/java8  
  
RUN yum -y update && yum install -y python-dev python-pip gcc make gcc-c++ \  
&& yum install -y libpng libjpeg ImageMagick GraphicsMagick \  
&& yum clean all  
  
# --------------------------------------------------------------- teamcity-
agent  
ENV TEAMCITY_VERSION 2017.2.1  
ENV TEAMCITY_GIT_PATH /usr/bin/git  
ENV AGENT_PORT 9090  
COPY buildAgent.zip /tmp/buildAgent.zip  
RUN unzip -qq /tmp/buildAgent.zip -d /srv/teamcity-agent  
  
COPY start-agent.sh /srv/  
  
RUN chmod +x /srv/teamcity-agent/bin/*.sh \  
&& chmod +x /srv/*.sh \  
&& mv /srv/teamcity-agent/conf/buildAgent.dist.properties /srv/teamcity-
agent/conf/buildAgent.properties \  
  
&& rm -fR /tmp/* \  
&& chown -R app:app /srv/teamcity-agent  
  
  
# -----------------------------------------------------------------------
nodejs  
ENV NODE_VERSION 8.9.4  
RUN (curl -L
http://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
| gunzip -c | tar x) \  
&& cp -R node-v${NODE_VERSION}-linux-x64/* /usr/ \  
&& rm -fR node-v${NODE_VERSION}-linux-x64 \  
&& npm update -g \  
&& npm install --unsafe-perm -g node-gyp aglio \  
&& npm install -g grunt gulp grunt-cli karma-cli  
  
RUN npm install -g yarn  
  
# ------------------------------------------------------------------------
maven  
ENV MAVEN_VERSION 3.5.2  
RUN (curl -L
http://www.us.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | gunzip -c | tar x) \  
&& mv apache-maven-$MAVEN_VERSION /opt/apache-maven  
  
ENV M2_HOME /opt/apache-maven  
ENV MAVEN_OPTS -Xmx512m -Xss256k -XX:+UseCompressedOops  
  
# ------------------------------------------------------------------------
Python PIP  
RUN pip install --upgrade pip  
  
# ------------------------------------------------------------------------
docker  
RUN yum install -y python-devel yum-utils jq && yum clean all \  
&& yum-config-manager --add-repo
https://download.docker.com/linux/centos/docker-ce.repo \  
&& yum install -y docker-ce \  
&& pip install --upgrade docker-compose  
ENV DOCKER_AVAILABLE=1  
# ------------------------------------------------------------------------
Python AWS & other tools  
RUN yum install jq \  
&& pip install --upgrade awscli  
ENV AWS_AVAILABLE=1  
# ------------------------------------------------------------------------ VCS  
RUN yum install -y git subversion  
ENV GIT_AVAILABLE=1  
ENV SVN_AVAILABLE=1  
RUN yum clean all  
  
EXPOSE ${AGENT_PORT}  
VOLUME /srv/teamcity-agent/conf  
USER app  
  
CMD ["/srv/start-agent.sh"]  

