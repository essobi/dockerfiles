FROM alpine:3.2  
MAINTAINER Andreas Linz "klingt.net@gmail.com"  
# install requirements  
RUN apk update &&\  
apk add python3\  
ffmpeg\  
flac\  
curl  
  
RUN pip3 install --upgrade pip &&\  
pip3 install cherrypy &&\  
pip3 install cherrymusic==0.37.1  
  
# set locale  
ENV LANG en_US.UTF-8  
ENV CM_USER cm  
  
# create user that runs cherrymusic  
RUN adduser -h /home/${CM_USER} -s /sbin/nologin -D ${CM_USER}  
RUN su -s /bin/sh ${CM_USER} -c "mkdir -p \  
~/.config/cherrymusic \  
~/.local/share/cherrymusic \  
~/basedir"  
  
EXPOSE 8080  
# mount your music folder into the basedir (docker run -v
/path/to/music:/home/cm/basedir)  
# and do the same for the config and share folder  
VOLUME /home/${CM_USER}/.config/cherrymusic \  
/home/${CM_USER}/.local/share/cherrymusic \  
/home/${CM_USER}/basedir  
  
WORKDIR /home/${CM_USER}  
CMD su -s /bin/sh -c 'cherrymusic' \- ${CM_USER}  

