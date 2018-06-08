FROM arubislander/openjdk  
MAINTAINER ArubIslander <arubislander@zonnet.nl>  
  
RUN apt-get update && apt-get install -y --no-install-recommends curl \  
ffmpeg \  
lame  
  
# create the following folder inside container  
RUN mkdir -p /var/media/music && \  
mkdir -p /var/media/podcasts && \  
mkdir -p /var/media/videos && \  
mkdir -p /var/media/pictures  
  
EXPOSE 4040  
VOLUME ["/var/media/music", "/var/media/podcasts", "/var/media/videos",
"/var/media/pictures"]  
  
WORKDIR /var/madsonic  
  
ENV S_USER madsonic  
  
RUN groupadd -r $S_USER && \  
useradd -r -g $S_USER $S_USER && \  
chown $S_USER /var/madsonic && \  
chown $S_USER -R /var/media  
  
USER $S_USER  
  
ENV S_VERSION 5.1.5260  
RUN curl -o /var/madsonic/madsonic-$S_VERSION-standalone.tar.gz \  
http://www.madsonic.org/download/5.1/20150831_madsonic-$S_VERSION-
standalone.tar.gz && \  
tar -zxvf madsonic-$S_VERSION-standalone.tar.gz && \  
rm madsonic-$S_VERSION-standalone.tar.gz && \  
mkdir ./transcode && \  
ln -s `which lame` ./transcode/lame && \  
ln -s `which ffmpeg` ./transcode/ffmpeg  
  
CMD /var/madsonic/madsonic.sh && \  
sleep 30 && \  
tail -F /var/madsonic/madsonic_sh.log  

