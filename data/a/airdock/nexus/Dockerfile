# VERSION 1.0  
# AUTHOR: Jerome Guibert <jguibert@gmail.com>  
# DESCRIPTION: Nexus Repository Manager  
# TO_BUILD: docker build --rm -t airdock/nexus .  
# SOURCE: https://github.com/airdock/docker-nexus  
FROM airdock/oracle-jdk:jre-1.8  
ENV NEXUS_HOME /srv/java/nexus  
ARG NEXUS_VERSION=2.14.2-01  
RUN apt-get update -qq && apt-get install -y --no-install-recommends ca-
certificates && \  
cd /tmp && curl -L -O
http://download.sonatype.com/nexus/oss/nexus-${NEXUS_VERSION}-bundle.tar.gz &&
\  
tar xvzf nexus-${NEXUS_VERSION}-bundle.tar.gz -C /srv/java && \  
ln -s /srv/java/nexus-${NEXUS_VERSION} /srv/java/nexus && \  
chown -R java:java /srv/java && \  
/root/post-install  
  
EXPOSE 8081  
VOLUME ["/srv/java/sonatype-work"]  
  
WORKDIR /srv/java/nexus  
  
CMD ["tini", "-g", "--", "gosu", "java:java", "/srv/java/nexus/bin/nexus",
"console"]  

