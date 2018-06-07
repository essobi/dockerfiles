FROM lsiobase/alpine.python  
MAINTAINER sparklyballs, ajw107 (Alex Wood)  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
# set python to use utf-8 rather than ascii  
ENV PYTHONIOENCODING="UTF-8"  
#add extra environment settings  
ENV CONFIG="/config"  
ENV APPDIRNAME="hydra"  
ENV APP_ROOT="/app"  
ENV APP_OPTS="--nobrowser --config=${CONFIG}/settings.cfg
--database=${CONFIG}/nzbhydra.db --logfile=${CONFIG}/nzbhydra.log"  
ENV APP_EXEC="nzbhydra.py"  
ENV APP_COMP="python"  
ENV GITURL="https://github.com/theotherp/nzbhydra.git"  
ENV GITBRANCH="master"  
#make life easy for yourself  
RUN apk update && \  
apk add nano git  
ENV TERM=xterm-color  
#RUN echo $'#!/bin/bash\nls -alF --color=auto --group-directories-first
--time-style=+"%H:%M %d/%m/%Y" --block-size="\'1" $@' > /usr/bin/ll  
# copy local files  
COPY root/ /  
RUN chmod +x /usr/bin/ll  
  
# ports and volumes  
EXPOSE 5075  
# WORKDIR /config/hydra  
#VOLUME /config /downloads  
VOLUME "${CONFIG}" /mnt  

