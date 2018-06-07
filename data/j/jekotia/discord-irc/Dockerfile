FROM jekotia/resin-raspberrypi3-alpine-node  
  
ENV TERM=screen-256color \  
LANG=C.UTF-8 \  
UID=2137 \  
GID=2137 \  
USER=nodejs \  
GROUP=nodejs \  
HOME=/home/nodejs \  
DATA=/data  
#  
##  
###  
RUN [ "cross-build-start" ]  
  
RUN npm install -g zlib-sync discordapp/erlpack uws \  
&& npm install -g discord.js \  
&& npm install -g discord-irc  
  
RUN mkdir -p $DATA \  
&& mkdir -p $HOME \  
&& chown -R $UID:$GID $HOME \  
&& chown -R $UID:$GID $DATA \  
&& addgroup \  
-g $GID \  
-S \  
$GROUP \  
&& adduser \  
-u $UID \  
-D \  
-S \  
-h $HOME \  
-s /sbin/nologin \  
-G $GROUP \  
$USER  
RUN [ "cross-build-end" ]  
###  
##  
#  
  
VOLUME $DATA  
  
WORKDIR $HOME  
  
USER $USER  
  
CMD /usr/local/bin/discord-irc --config /data/discord-irc.json  

