# This Dockerfile is used to build the production bundle for a Meteor app.  
ARG METEOR_VERSION="1.6.0.1"  
ARG NODE_VERSION="8.9.3"  
ARG APP_DIR="/usr/share/meteor-app"  
ARG GIT_COMMIT=""  
FROM ubuntu:16.04 AS build  
LABEL maintainer="Xingchen Hong <hello@xc-h.com>"  
  
RUN apt-get update \  
&& apt-get install -y -q build-essential \  
libssl-dev curl git \  
python-dev \  
&& apt-get install -y -q locales \  
&& locale-gen en_US.UTF-8 \  
&& localedef -i en_GB -f UTF-8 en_US.UTF-8 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV HOME="/home/meteor"  
ARG APP_DIR  
  
RUN useradd -m -s /bin/bash meteor \  
&& mkdir -p "${APP_DIR}" \  
&& chown -R meteor:meteor "${APP_DIR}"  
  
#! TODO: Use the line below to replace the workaround when `17.09` is landed  
# on Docker Cloud.  
# See https://github.com/moby/moby/issues/35731#issuecomment-360666913  
#  
# ADD --chown=meteor:meteor ./meteor-app "${APP_DIR}/source"  
#  
#! Workaround begins.  
ADD ./meteor-app "${APP_DIR}/source"  
RUN chown -R meteor:meteor "${APP_DIR}/source"  
#! End of workaround.  
USER meteor  
  
# Install Meteor.  
ARG METEOR_VERSION  
  
RUN curl "https://install.meteor.com/?release=${METEOR_VERSION}" | sh  
ENV METEOR_PATH="${HOME}/.meteor"  
ENV PATH="$PATH:$METEOR_PATH"  
RUN cd "${APP_DIR}/source" \  
&& meteor npm install --production --unsafe-perm \  
&& meteor build "${APP_DIR}" \--directory --architecture os.linux.x86_64  
  
FROM node:${NODE_VERSION}-slim  
LABEL maintainer="Xingchen Hong <hello@xc-h.com>"  
  
RUN apt-get update \  
&& apt-get install -y -q build-essential \  
libssl-dev curl git \  
python-dev \  
&& apt-get install -y -q locales \  
&& locale-gen en_US.UTF-8 \  
&& localedef -i en_GB -f UTF-8 en_US.UTF-8 \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ARG APP_DIR  
  
ENV HOME="/home/meteor"  
RUN useradd -m -s /bin/bash meteor \  
&& mkdir -p "${APP_DIR}" \  
&& chown -R meteor:meteor "${APP_DIR}"  
WORKDIR "${APP_DIR}"  
  
ARG GIT_COMMIT  
  
# Meteor Port Config  
ENV NODE_ENV="production" \  
ROOT_URL="http://localhost" \  
MONGO_URL="mongodb://localhost" \  
METEOR_SETTINGS='{"public":{}}' \  
PORT=3000 \  
BUILD_GIT_COMMIT="${GIT_COMMIT}"  
#! TODO: Use the lines below to replace the workaround when `17.09` is landed  
# on Docker Cloud.  
# See https://github.com/moby/moby/issues/35731#issuecomment-360666913  
#  
# COPY --from=build --chown=meteor:meteor "${APP_DIR}/bundle"
"${APP_DIR}/bundle"  
# ADD --chown=meteor:meteor ./meteor-app.settings.default.json
"${APP_DIR}/app-settings.json"  
# ADD --chown=meteor:meteor ./Dockerfile.entrypoint.sh
"${APP_DIR}/entrypoint.sh"  
#  
#! Workaround begins.  
COPY \--from=build "${APP_DIR}/bundle" "${APP_DIR}/bundle"  
ADD ./meteor-app.settings.default.json "${APP_DIR}/app-settings.json"  
ADD ./Dockerfile.entrypoint.sh "${APP_DIR}/entrypoint.sh"  
RUN chown -R meteor:meteor "${APP_DIR}"  
#! End of workaround.  
USER meteor  
ENTRYPOINT bash entrypoint.sh  

