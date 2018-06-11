FROM openjdk:8-jre-alpine  
  
ENV GERRIT_HOME /home/gerrit  
ENV GERRIT_LIB /var/lib/gerrit  
ENV GERRIT_SITE ${GERRIT_HOME}/site  
ENV GERRIT_USER gerrit  
ENV GERRIT_GROUP gerrit  
ENV GERRIT_WAR ${GERRIT_LIB}/gerrit.war  
ENV GERRIT_VERSION 2.13.4  
ENV GERRIT_PLUGIN_VERSION stable-2.13  
RUN apk add --no-cache openssh openssl git su-exec && \  
addgroup -S "$GERRIT_GROUP" && \  
adduser -S -D -h "$GERRIT_HOME" -G "$GERRIT_GROUP" "$GERRIT_USER" && \  
mkdir -p "$GERRIT_LIB" && chown -R "$GERRIT_USER":"$GERRIT_GROUP"
"$GERRIT_LIB"  
  
USER "$GERRIT_USER"  
RUN wget "https://gerrit-
releases.storage.googleapis.com/gerrit-$GERRIT_VERSION.war" \  
-O "$GERRIT_WAR"  
  
# Let's download plugins from a random CI on the Internet  
RUN mkdir -p "$GERRIT_LIB/plugins/" && \  
wget "https://gerrit-ci.gerritforge.com/job/plugin-delete-
project-$GERRIT_PLUGIN_VERSION/lastSuccessfulBuild/artifact/buck-
out/gen/plugins/delete-project/delete-project.jar" \  
-O "$GERRIT_LIB/plugins/delete-project.jar"  
  
COPY gerrit.config "$GERRIT_LIB/gerrit-initial.config"  
COPY replication.config "$GERRIT_LIB/replication-initial.config"  
  
COPY run.sh "$GERRIT_LIB/run.sh"  
COPY start-gerrit.sh "$GERRIT_LIB/start-gerrit.sh"  
  
USER root  
  
VOLUME "$GERRIT_HOME"  
  
EXPOSE 8080 29418  
ENTRYPOINT "$GERRIT_LIB/run.sh"  

