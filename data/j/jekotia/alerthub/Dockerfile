FROM jekotia/resin-raspberrypi3-alpine-node  
  
ENV TERM=screen-256color \  
LANG=C.UTF-8 \  
UID=2041 \  
GID=2041 \  
USER=nodejs \  
GROUP=nodejs \  
DATA=/data \  
HOME=/home/nodejs \  
APPDIR=/home/nodejs/alerthub \  
CONFIG=/home/nodejs/alerthub/etc/config.js  
#  
##  
###  
RUN [ "cross-build-start" ]  
RUN mkdir -p $HOME \  
&& mkdir -p $DATA \  
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
  
RUN apk add --no-cache \  
git \  
su-exec  
  
RUN su-exec $USER:$GROUP git clone https://github.com/Ardakilic/alerthub.git
$APPDIR \  
&& cd $APPDIR \  
&& su-exec $USER:$GROUP npm install \  
&& su-exec $USER:$GROUP npm run init \  
&& rm -f $CONFIG \  
&& ln -sf /data/config.js $CONFIG \  
&& chown -R $UID:$GID $HOME \  
&& chown -R $UID:$GID $DATA  
  
RUN [ "cross-build-end" ]  
###  
##  
#  
VOLUME $DATA/config.js  
  
USER $USER  
WORKDIR $APPDIR  
CMD npm start  

