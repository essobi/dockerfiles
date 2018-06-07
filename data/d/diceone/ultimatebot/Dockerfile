FROM alpine:3.4  
MAINTAINER Dr. Doom <doom@dev-ops.de>  
  
ENV HUBOT_NAME Hubot  
ENV HUBOT_PATH /app  
ENV HUBOT_USER postgres  
ENV HUBOT_OWNER='Bot Wrangler <bw@example.com>'  
ENV HUBOT_DESCRIPTION='Delightfully aware robutt'  
  
ENV HUBOT_NPM_SCRIPTS='hubot-google-images hubot-reaction hubot-standup-alarm
hubot-youtube hubot-urban hubot-shipping-forecast hubot-business-cat hubot-
tell hubot-motivate hubot-graphme hubot-jenkins-slack hubot-jenkins hubot-cron
hubot-auth hubot-shell hubot-bookmark hubot-bofh hubot-maps hubot-grafana
hubot-datadog hubot-ansible hubot-redis-brain hubot-diagnostics hubot-rss-
reader'  
ENV HUBOT_EXTERNAL_SCRIPTS='["hubot-help", "hubot-google-images", "hubot-
shipit", "hubot-reaction","hubot-standup-alarm","hubot-youtube","hubot-
urban","hubot-shipping-forecast","hubot-business-cat","hubot-tell","hubot-
motivate","hubot-graphme","hubot-jenkins-slack","hubot-jenkins","hubot-
cron","hubot-auth","hubot-shell","hubot-bookmark","hubot-bofh","hubot-
maps","hubot-grafana","hubot-datadog","hubot-ansible","hubot-redis-
brain","hubot-diagnostics","hubot-rss-reader"]'  
  
WORKDIR ${HUBOT_PATH}  
  
RUN chown -R ${HUBOT_USER} ${HUBOT_PATH} && \  
apk add \--update nodejs && \  
rm -rf /var/cache/apk/* && \  
npm install -g hubot coffee-script yo generator-hubot && \  
rm -rf ~/.npm && \  
npm cache clear  
  
USER postgres  
ENV HOME ${HUBOT_PATH}  
RUN yo hubot \--owner="${HUBOT_OWNER}" \--name="${HUBOT_USER}"
\--description="${HUBOT_DESCRIPTION}" \--adapter=slack && \  
npm install hubot-slack \--save && \  
rm hubot-scripts.json && \  
npm install ${HUBOT_NPM_SCRIPTS} \--save && \  
echo ${HUBOT_EXTERNAL_SCRIPTS} > external-scripts.json && \  
rm -rf ~/.npm && \  
npm cache clear  
  
ENTRYPOINT ["/bin/sh", "-c", "bin/hubot -a slack -n '$HUBOT_NAME'"]  

