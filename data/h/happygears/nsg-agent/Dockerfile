  
FROM maven:3-jdk-8-slim as build  
  
RUN apt-get -y update && apt-get install -y git rpm file findutils  
  
RUN rm -rf /usr/src/app && mkdir -p /usr/src/app  
COPY pom.xml /usr/src/app  
COPY src /usr/src/app/src  
COPY doc /usr/src/app/doc  
COPY lib /usr/src/app/lib  
COPY .git /usr/src/app/  
  
WORKDIR /usr/src/app  
  
# This builds the jar and rpm, even though the rpm is not used in docker
images.  
# The rpm is built using maven-rpm-plugin during "mvn package" phase. I am
keeping  
# it here because I think I might switch to building the rpm and deb packages  
# in docker containers in the future.  
#  
# Deb package is built using fpm (see script build-packages.sh) and is not  
# built in docker at this time  
#  
RUN mvn package -B  
  
#############################################################################  
FROM openjdk:8-jdk-slim  
  
ENV NSG_CURRENT="/opt/nsg-agent/current"  
ENV NSG_HOME="/opt/nsg-agent/home"  
RUN apt-get -y update && apt-get install -y iputils-ping fping sed jsvc
traceroute rsyslog rsyslog-relp less procps && apt-get clean all  
  
RUN mkdir -p $NSG_HOME/ && \  
mkdir -p $NSG_CURRENT/bin/ && \  
mkdir -p $NSG_CURRENT/doc/ && \  
mkdir -p $NSG_CURRENT/lib/  
  
COPY \--from=build /usr/src/app/target/nsg-agent-*.jar $NSG_CURRENT/lib/  
COPY \--from=build /usr/src/app/target/lib/* $NSG_CURRENT/lib/  
COPY \--from=build /usr/src/app/target/classes/*.sh $NSG_CURRENT/bin/  
COPY \--from=build /usr/src/app/target/classes/agent.conf $NSG_HOME  
  
COPY \--from=build /usr/src/app/src/main/bash/run.sh /  
  
COPY doc/* $NSG_CURRENT/doc/  
COPY lib/* $NSG_CURRENT/lib/  
  
# create this directory early to make sure it is chown'd to nw2  
RUN mkdir -p ${NSG_HOME}/data/kafka/ssl  
  
RUN useradd --system -s /bin/bash -U -m --home-dir ${NSG_HOME} nw2  
#RUN useradd -ms /bin/bash nw2  
RUN chmod +x $NSG_CURRENT/bin/*  
RUN chown -R nw2.nw2 $NSG_HOME && chown -R nw2.nw2 $NSG_CURRENT  
RUN chown -R nw2.nw2 /var/spool/rsyslog  
  
USER nw2  
  
CMD exec /run.sh  
  

