FROM node:latest  
MAINTAINER laninabox <info@utopit.be>  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION=latest  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="hubot_discord" \  
org.label-schema.description="Run Hubot with the Discord adapter in Docker" \  
org.label-schema.url="https://hubot.github.io/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://bitbucket.org/laninabox/docker-
hubot_discord" \  
org.label-schema.vendor="None" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
# Environment variables  
ARG ARG_HUBOT_NAME="towerbot"  
ENV HUBOT_NAME=$ARG_HUBOT_NAME  
ENV HUBOT_DISCORD_TOKEN=yourtokenhere  
ENV HUBOT_DISCORD_MAX_MESSAGE_LENGTH=2000  
# NPM specifics  
ENV NPM_CONFIG_PREFIX=~/.npm-global  
ENV PATH="$HOME/.npm-global/bin:$PATH"  
# Create hubot user and link from nodejs to node  
RUN useradd -d /hubot -m -s /bin/bash -U hubot && \  
ln -s /usr/bin/nodejs /usr/bin/node  
  
# Log in as hubot user and change directory  
USER hubot  
WORKDIR /hubot  
  
# NPM setup  
RUN npm install -g yo generator-hubot  
  
# Install hubot  
RUN ~/.npm-global/bin/yo hubot --owner="laninabox" \--name="HuBot"
\--description="HuBot on Docker" \--defaults  
  
# install discord adapter and peer dependencies  
RUN npm install bufferutil@^3.0.2 \  
erlpack@hammerandchisel/erlpack \  
node-opus@^0.2.6 \  
opusscript@^0.0.3 \  
sodium@^2.0.1 \  
libsodium-wrappers@^0.5.4 \  
uws@^0.14.5 \  
coffee-script@^1.12.6 \  
https://github.com/idehub/hubot-discord \  
\--save  
  
# Run hubot  
ENTRYPOINT ["bin/hubot"]  
CMD ["-a", "discord", "--name", "${HUBOT_NAME}"]  
  

