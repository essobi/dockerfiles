FROM arubislander/openjdk  
MAINTAINER ArubIslander <arubislander@zonnet.nl>  
  
RUN apt-get update && apt-get install -y --no-install-recommends curl \  
ffmpeg \  
lame  
  
# create the following folder inside container  
RUN mkdir -p /var/media/music && \  
mkdir -p /var/media/podcasts && \  
mkdir -p /var/media/videos && \  
mkdir -p /var/media/pictures && \  
mkdir -p /var/media/playlists  
  
EXPOSE 4040  
  
VOLUME ["/var/media/music", \  
"/var/media/podcasts", \  
"/var/media/videos", \  
"/var/media/pictures", \  
"/var/media/playlists"]  
  
WORKDIR /var/subsonic  
  
ENV S_USER subsonic  
  
RUN groupadd -r $S_USER && \  
useradd -r -g $S_USER $S_USER && \  
chown $S_USER /var/subsonic && \  
chown $S_USER -R /var/media  
  
USER $S_USER  
  
ENV S_VERSION 6.1.2  
  
RUN curl -o /var/subsonic/subsonic-$S_VERSION-standalone.tar.gz \  
https://s3-eu-west-1.amazonaws.com/subsonic-
public/download/subsonic-$S_VERSION-standalone.tar.gz && \  
tar -zxvf subsonic-$S_VERSION-standalone.tar.gz && \  
rm subsonic-$S_VERSION-standalone.tar.gz  
RUN mkdir ./transcode && \  
ln -s `which lame` ./transcode/lame && \  
ln -s `which ffmpeg` ./transcode/ffmpeg  
RUN sed -i "s/\/var\/music$/\/var\/media\/music/;\  
s/\/var\/music\/Podcast$/\/var\/media\/podcasts/;\  
s/\/var\/playlists$/\/var\/media\/playlists/" subsonic.sh  
  
CMD /var/subsonic/subsonic.sh && \  
sleep 30 && \  
tail -F /var/subsonic/subsonic_sh.log  

