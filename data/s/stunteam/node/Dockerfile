# Reference: https://docs.docker.com/engine/reference/builder/  
### DOCKER INSTRUCTIONS  
# =====================  
# Get build stage image variables.  
ARG IMAGE  
ARG TAG  
  
# Initialize a new build stage.  
# Future release: FROM --platform=linux
${IMAGE:-stunteam/alpine}:${TAG:-latest}  
FROM ${IMAGE:-stunteam/alpine}:${TAG:-latest}  
  
# Sets used shell path.  
ARG SHELL  
ENV SHELL ${SHELL:-"/bin/sh"}  
  
# Sets application context directory.  
ARG APP_CONTEXT  
ENV APP_CONTEXT ${APP_CONTEXT:-.}  
  
# Sets application working directory.  
ARG APP_WORKDIR  
ENV APP_WORKDIR ${APP_WORKDIR:-/usr/src/app}  
  
# Sets application user name.  
ARG APP_USER  
ENV APP_USER ${APP_USER:-node}  
  
# Sets application user group name.  
ARG APP_USER_GROUP  
ENV APP_USER_GROUP ${APP_USER_GROUP:-$APP_USER}  
  
# Sets application user home path.  
ARG APP_USER_HOME  
ENV APP_USER_HOME ${APP_USER_HOME:-/home/$APP_USER}  
  
# Sets application modules directory.  
ARG APP_MODULES  
ENV APP_MODULES ${APP_MODULES:-$APP_WORKDIR/node_modules}  
  
# Sets system packages to add.  
ARG PKGS  
ENV PKGS ${PKGS:-}  
  
# Sets Node.js packages to global add.  
ARG APP_PKGS  
ENV APP_PKGS ${APP_PKGS:-}  
  
  
# Add metadata to an image.  
LABEL maintainer=$MAINTAINER  
LABEL name="stunteam-docker-node"  
LABEL version="1.0"  
LABEL description="Docker image based on latest Alpine Edge and with latest
Node.js and Yarn."  
  
### SYSTEM INSTRUCTIONS  
# =====================  
# Update the repositories file.  
RUN $RUN_PRINT "Update the repositories file." \  
; apk update  
  
# Add non-sudo application user and his group.  
RUN $RUN_PRINT "Add non-sudo application user and his group." \  
; addgroup -g 1000 $APP_USER \  
&& adduser -h $APP_USER_HOME -g "Application User" -s $SHELL -G
$APP_USER_GROUP -D -u 1000 $APP_USER  
  
# Add Node.js and Yarn.  
RUN $RUN_PRINT "Add Node.js and Yarn." \  
; apk add --no-cache --progress libuv nodejs yarn \  
&& $RUN_PRINT_END "Versions installed: node.js $(node -v), yarn v$(yarn -v)."  
  
# Add additional system dependencies if predefined.  
RUN $RUN_PRINT "Add additional system dependencies if defined." \  
; if ! [ -z $PKGS ]; then apk add --no-cache --progress $PKGS; fi  
  
# Add Node.js global packages if predefined.  
RUN $RUN_PRINT "Add Node.js global packages if predefined." \  
; if ! [ -z $APP_PKGS ]; then yarn global add --force --check-files --non-
interactive $APP_PKGS; fi  
  
# Set working directory.  
WORKDIR $APP_WORKDIR  
  
# Clean up from unnecessary files.  
RUN $RUN_PRINT "Clean up from unnecessary files"; $RUN_CLEANUP \  
/usr/lib/node_modules/npm/man \  
/usr/lib/node_modules/npm/doc \  
/usr/lib/node_modules/npm/changelog \  
/usr/lib/node_modules/npm/scripts \  
/usr/lib/node_modules/npm/html  
  
# Provide defaults for an executing container.  
CMD [ "node" ]  
  
### ONBUILD INSTRUCTIONS  
# ======================  
# Export environment variables to child images.  
ONBUILD ENV RUN_PRINT $RUN_PRINT  
ONBUILD ENV RUN_PRINT_END $RUN_PRINT_END  
ONBUILD ENV RUN_CLEANUP $RUN_CLEANUP  
ONBUILD ENV RUN_UPGRADE $RUN_UPGRADE  
ONBUILD ENV MAINTAINER $MAINTAINER  
ONBUILD ENV APP_CONTEXT $APP_CONTEXT  
ONBUILD ENV APP_WORKDIR $APP_WORKDIR  
ONBUILD ENV APP_USER $APP_USER  
ONBUILD ENV APP_USER_GROUP $APP_USER_GROUP  
ONBUILD ENV APP_USER_HOME $APP_USER_HOME  
ONBUILD ENV APP_MODULES $APP_MODULES  
  
# Update the Alpine repositories file.  
ONBUILD RUN $RUN_PRINT "Update the Alpine repositories file."; apk update  
  
### BUILDING AND RUNNING COMMANDS  
# ===============================  
#### Build image /wo compression  
# docker build --platform linux -t stunteam/node:latest .  

