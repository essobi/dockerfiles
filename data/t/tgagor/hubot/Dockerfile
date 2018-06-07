FROM node:7.3  
MAINTAINER tgagor, https://github.com/tgagor  
  
# EXPOSE 8080/tcp  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
COPY ./files/runsvdir-start /usr/local/sbin/runsvdir-start  
RUN apt-get update \  
&& apt-get install --yes --force-yes runit \  
&& chmod +x /usr/local/sbin/runsvdir-start \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV HUBOT_HOME /opt/hubot  
ENV HUBOT_LOG /var/log/hubot  
ENV HUBOT_NAME hu  
ENV HUBOT_ADAPTER slack  
ENV HUBOT_DESC "Helpful robot"  
ENV HUBOT_OWNER "tgagor <tg@tg>"  
ENV HUBOT_JENKINS_URL "http://localhost:8080"  
ENV HUBOT_JENKINS_AUTH "user:password"  
ENV HUBOT_GRAFANA_HOST "http://play.grafana.org"  
ENV HUBOT_GRAFANA_API_KEY "API key"  
ENV HUBOT_GRAFANA_QUERY_TIME_RANGE "6h"  
ENV HUBOT_SLACK_TOKEN "check here https://slackapi.github.io/hubot-slack/"  
ENV HUBOT_SLACK_INCOMING_WEBHOOK "check here
https://my.slack.com/services/new/incoming-webhook"  
ENV NODE_ENV production  
  
# prepare unprivileged user for hubot  
RUN groupadd -g 1100 hubot \  
&& useradd -ms /bin/bash -u 1100 -g hubot -d "$HUBOT_HOME" hubot \  
&& mkdir -p "$HUBOT_HOME" \  
&& mkdir -p "$HUBOT_LOG" \  
&& chown -R hubot:hubot "$HUBOT_HOME"  
  
# install generator-hubot  
RUN npm install -g yo generator-hubot  
  
USER hubot  
WORKDIR $HUBOT_HOME  
  
RUN cd "$HUBOT_HOME" \  
&& yo hubot --owner="$HUBOT_OWNER" \  
\--name="$HUBOT_NAME" \  
\--description="$HUBOT_DESC" \  
\--adapter="$HUBOT_ADAPTER" \  
\--defaults  
  
RUN npm install --save \  
hubot-jenkins-slack hubot-jenkins \  
hubot-grafana hubot-slack-attachment  
  
COPY ./files/hubot/external-scripts.json "$HUBOT_HOME"  
# ADD ./files/hubot/scripts "$HUBOT_HOME"  
RUN rm -f "$HUBOT_HOME/hubot-scripts.json"  
  
# copy runit configs  
USER root  
COPY ./files/etc /etc  
ENTRYPOINT ["/usr/local/sbin/runsvdir-start"]  

