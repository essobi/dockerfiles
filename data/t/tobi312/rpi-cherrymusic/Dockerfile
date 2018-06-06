FROM resin/raspberry-pi2-python:3.6  
MAINTAINER Tobias Hargesheimer <docker@ison.ws>  
  
ENV APP_USER=pi  
  
RUN [ "cross-build-start" ]  
  
RUN apt-get update && apt-get install -y \  
git \  
lame \  
vorbis-tools \  
flac \  
faad \  
mpg123 \  
opus-tools \  
#ffmpeg \  
imagemagick \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install unidecode cherrypy  
  
COPY run.sh /home/$APP_USER/  
RUN chmod +x /home/$APP_USER/run.sh  
  
RUN useradd -ms /bin/bash $APP_USER  
  
RUN mkdir -p /home/$APP_USER/git && cd /home/$APP_USER/git && git clone
https://github.com/devsnd/cherrymusic.git cherrymusic/  
RUN mkdir -p /home/$APP_USER/Music && mkdir -p
/home/$APP_USER/.config/cherrymusic && mkdir -p
/home/$APP_USER/.local/share/cherrymusic && mkdir -p /home/$APP_USER/.ssl  
  
COPY cherrymusic.conf /home/$APP_USER/.config/cherrymusic/cherrymusic.conf  
  
RUN chown -R $APP_USER:$APP_USER /home/$APP_USER/  
  
RUN [ "cross-build-end" ]  
  
USER $APP_USER  
#WORKDIR /home/$APP_USER/git/cherrymusic  
VOLUME /home/$APP_USER/.config/cherrymusic
/home/$APP_USER/.local/share/cherrymusic /home/$APP_USER/.ssl
/home/$APP_USER/Music  
EXPOSE 7600/tcp 7700/tcp  
  
ENTRYPOINT ["/home/pi/run.sh"]  
CMD python3 /home/pi/git/cherrymusic/cherrymusic  

