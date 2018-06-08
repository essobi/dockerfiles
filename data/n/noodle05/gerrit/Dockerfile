FROM openjdk:8-jre-alpine  
  
MAINTAINER Wei Gao <wei@gaofamily.org>  
  
# Overridable defaults  
ENV GERRIT_HOME=/var/gerrit  
ENV GERRIT_CACHE_DIR=${GERRIT_HOME}/cache  
ENV GERRIT_SITE=${GERRIT_HOME}/review_site  
ENV GERRIT_WAR=${GERRIT_HOME}/gerrit.war  
ENV GERRIT_VERSION=2.14.6  
ENV GERRIT_USER=gerrit2  
ENV GERRIT_INIT_ARGS=""  
ENV PLUGIN_VERSION=stable-2.14  
ENV GERRITFORGE_URL=https://gerrit-ci.gerritforge.com  
ENV GERRITFORGE_ARTIFACT_DIR=lastSuccessfulBuild/artifact/bazel-
genfiles/plugins  
ENV BOUNCY_CASTLE_VERSION=154  
ENV BOUNCY_CASTLE_URL=https://downloads.bouncycastle.org/java  
  
COPY gerrit-entrypoint.sh /  
COPY gerrit-start.sh /  
  
# Add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN adduser -u 100 -D -h "$GERRIT_HOME" -S $GERRIT_USER && \  
apk add --no-cache git-gitweb su-exec perl-cgi && \  
apk add --no-cache --virtual .build-deps curl && \  
mkdir /docker-entrypoint-init.d && \  
curl -Ls https://gerrit-
releases.storage.googleapis.com/gerrit-${GERRIT_VERSION}.war -o $GERRIT_WAR &&
\  
curl -Ls ${GERRITFORGE_URL}/job/plugin-delete-project-
bazel-${PLUGIN_VERSION}/${GERRITFORGE_ARTIFACT_DIR}/delete-project/delete-
project.jar -o ${GERRIT_HOME}/delete-project.jar && \  
curl -Ls ${GERRITFORGE_URL}/job/plugin-events-log-
bazel-${PLUGIN_VERSION}/${GERRITFORGE_ARTIFACT_DIR}/events-log/events-log.jar
-o ${GERRIT_HOME}/events-log.jar && \  
curl -Ls ${GERRITFORGE_URL}/job/plugin-oauth-bazel-
master-${PLUGIN_VERSION}/${GERRITFORGE_ARTIFACT_DIR}/oauth/oauth.jar -o
${GERRIT_HOME}/oauth.jar && \  
curl -Ls ${BOUNCY_CASTLE_URL}/bcprov-jdk15on-${BOUNCY_CASTLE_VERSION}.jar -o
${GERRIT_HOME}/bcprov-jdk15on-${BOUNCY_CASTLE_VERSION}.jar && \  
curl -Ls ${BOUNCY_CASTLE_URL}/bcpkix-jdk15on-${BOUNCY_CASTLE_VERSION}.jar -o
${GERRIT_HOME}/bcpkix-jdk15on-${BOUNCY_CASTLE_VERSION}.jar && \  
su-exec ${GERRIT_USER} mkdir -p $GERRIT_SITE && \  
su-exec ${GERRIT_USER} mkdir -p $GERRIT_CACHE_DIR && \  
apk del .build-deps && \  
rm -fr .build-deps && \  
rm -fr /tmp/hsprefdata_root  
  
#Gerrit site directory is a volume, so configuration and repositories  
#can be persisted and survive image upgrades.  
VOLUME $GERRIT_SITE $GERRIT_CACHE_DIR  
  
ENTRYPOINT ["/gerrit-entrypoint.sh"]  
  
EXPOSE 8080 29418  
CMD ["start"]  

