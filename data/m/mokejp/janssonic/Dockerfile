FROM vyolin/alpine-maven:latest  
  
RUN apk --update add git ffmpeg flac lame && \  
git clone --depth 1 -b janssonic https://github.com/Der-Jan/supersonic.git
/tmp/subsonic && \  
cd /tmp/subsonic && \  
mvn install -P full && \  
cd subsonic-assembly && \  
mvn assembly:assembly && \  
mkdir -p /opt/subsonic && \  
mv target/subsonic-6.0-standalone.tar.gz /opt/subsonic && \  
cd /opt/subsonic && \  
tar zxvf subsonic-6.0-standalone.tar.gz && \  
mkdir -p /var/subsonic && \  
chown -R nobody:users /var/subsonic && \  
mkdir -p /var/playlists && \  
chown -R nobody:users /var/playlists && \  
mkdir -p /opt/subsonic/transcode && \  
ln -s /usr/bin/lame /opt/subsonic/transcode/lame && \  
ln -s /usr/bin/ffmpeg /opt/subsonic/transcode/ffmpeg && \  
rm -rf /tmp/* && \  
rm -rf /root/.m2 && \  
apk del git && \  
rm -rf /var/cache/apk/* && \  
adduser nobody users  
  
USER nobody  
VOLUME ["/var/subsonic"]  
VOLUME ["/var/music"]  
VOLUME ["/var/playlists"]  
  
EXPOSE 4040  
  
CMD /opt/subsonic/subsonic.sh && sleep 5 && tail -f
/var/subsonic/subsonic_sh.log  
  

