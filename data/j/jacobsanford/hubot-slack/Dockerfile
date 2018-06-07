FROM node:8-alpine  
MAINTAINER Jacob Sanford <jsanford_at_unb.ca>  
  
ARG HUBOT_OWNER="Bot Wrangler <bw@example.com>"  
ARG HUBOT_DESCRIPTION="Delightfully aware robutt"  
ARG HUBOT_NPM_SCRIPTS="hubot-google-images hubot-reaction"  
ARG HUBOT_EXTERNAL_SCRIPTS='["hubot-help", "hubot-google-images", "hubot-
shipit", "hubot-reaction"]'  
  
ENV HUBOT_NAME Hubot  
ENV HUBOT_PATH /app  
ENV HUBOT_USER postgres  
  
RUN mkdir ${HUBOT_PATH} && chown -R ${HUBOT_USER} ${HUBOT_PATH} && \  
npm install -g hubot coffee-script yo generator-hubot && \  
rm -rf ~/.npm  
  
USER postgres  
WORKDIR ${HUBOT_PATH}  
ENV HOME ${HUBOT_PATH}  
RUN yo hubot \--owner="${HUBOT_OWNER}" \--name="${HUBOT_USER}"
\--description="${HUBOT_DESCRIPTION}" \--adapter=slack && \  
npm install hubot-slack --save && \  
rm hubot-scripts.json && \  
npm install ${HUBOT_NPM_SCRIPTS} \--save && \  
echo ${HUBOT_EXTERNAL_SCRIPTS} > external-scripts.json && \  
rm -rf ~/.npm  
  
ENTRYPOINT ["/bin/sh", "-c", "bin/hubot -a slack -n '$HUBOT_NAME'"]  

