FROM williamyeh/java8  
MAINTAINER Alexander Dvorkovyy  
  
## Teamcity  
ARG AGENT_DIR=/opt/buildAgent  
ARG AGENT_HOME=/home/teamcity  
  
COPY ./teamcity-agent.sh /teamcity-agent.sh  
  
RUN apt-get update \  
&& apt-get install -y curl git unzip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir -p $AGENT_DIR \  
&& addgroup --system --gid 990 teamcity \  
&& adduser --system --uid 990 --gid 990 --home $AGENT_HOME \--shell /bin/false
teamcity \  
&& chown teamcity:teamcity $AGENT_DIR \  
&& sed -i 's#%AGENT_DIR%#'$AGENT_DIR'#' /teamcity-agent.sh \  
&& chmod +x /teamcity-agent.sh  
  
WORKDIR $AGENT_DIR  
VOLUME $AGENT_HOME  
VOLUME $AGENT_DIR  
  
# Environment variables, safe to change in container  
ENV TEAMCITY_AGENT_PORT 9090  
ENV TEAMCITY_SERVER "http://teamcity:8111"  
EXPOSE $TEAMCITY_AGENT_PORT  
  
## Docker  
ARG DOCKER_VERSION=1.12.1  
ARG
DOCKER_SHA256=05ceec7fd937e1416e5dce12b0b6e1c655907d349d52574319a1e875077ccb79  
ARG DOCKER_COMPOSE_VERSION=1.8.1  
RUN curl -fSL
"https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz" -o
docker.tgz \  
&& echo "${DOCKER_SHA256} *docker.tgz" | sha256sum -c - \  
&& tar -xzvf docker.tgz \  
&& mv docker/* /usr/local/bin/ \  
&& rmdir docker \  
&& rm docker.tgz \  
&& docker -v \  
&& curl -fsSL
"https://github.com/docker/compose/releases/download/$DOCKER_COMPOSE_VERSION/docker-
compose-Linux-x86_64" -o /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose  
ENV TEAMCITY_AGENT_NAME "SBT_Agent"  
ENV SBT_VERSION 0.13.12  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
  
RUN curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local && \  
echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built  
  
USER teamcity  
  
RUN echo "==> fetch all sbt jars from Maven repo..." \  
&& sbt  
  
CMD ["/teamcity-agent.sh"]  

