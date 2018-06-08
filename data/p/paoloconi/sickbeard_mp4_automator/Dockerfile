FROM lsiobase/alpine.python:3.6  
MAINTAINER sparklyballs  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="Linuxserver.io version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
# set python to use utf-8 rather than ascii  
ENV PYTHONIOENCODING="UTF-8"  
# install app  
RUN \  
git clone \--depth 1 git://github.com/midgetspy/Sick-Beard.git /app/sickbeard  
  
# add local files  
COPY root/ /  
  
### Script to be used with LinuxServer.io DockerBase Image of NZBGet  
### Will install MP4Automator
(https://github.com/mdhiggins/sickbeard_mp4_automator) and Dependencies  
RUN apk update  
RUN apk upgrade  
  
RUN apk add git  
RUN apk add ffmpeg  
  
RUN curl https://bootstrap.pypa.io/ez_setup.py -o - | python  
RUN easy_install pip  
  
RUN pip install requests  
RUN pip install requests[security] ###???  
RUN pip install requests-cache  
RUN pip install babelfish  
RUN pip install 'guessit<2'  
RUN pip install 'subliminal<2'  
# RUN pip uninstall stevedore  
RUN pip install 'stevedore==1.19.1'  
RUN pip install python-dateutil  
# pip install deluge-client  
RUN pip install qtfaststart  
  
##Get MP4Automator  
RUN [[ ! -d /mp4automator/.git ]] && (git clone
git://github.com/mdhiggins/sickbeard_mp4_automator.git /mp4automator && chown
-R abc:abc /mp4automator)  
  
##Use .ini if present or copy sample  
RUN [[ ! -f /mp4automator/autoProcess.ini ]] && (cp
/mp4automator/autoProcess.ini.sample /mp4automator/autoProcess.ini)  
  
# test if updates have been disabled  
# RUN [ "$ADVANCED_DISABLEUPDATES" ] && exit 0  
WORKDIR /mp4automator  
RUN git pull  
RUN chown -R abc:abc /config  
  
# ports and volumes  
EXPOSE 8081  
VOLUME /config /downloads /tv /mp4automator  

