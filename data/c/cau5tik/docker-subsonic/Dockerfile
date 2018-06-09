FROM ubuntu  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
apt-get update && \  
apt-get install -y --no-install-recommends --no-install-suggests
openjdk-8-jre-headless nfs-common locales && \  
apt-get clean && \  
useradd -M subsonic && \  
usermod -aG subsonic subsonic  
  
ENV SUBSONIC_VERSION 6.0  
ADD
http://downloads.sourceforge.net/project/subsonic/subsonic/$SUBSONIC_VERSION/subsonic-$SUBSONIC_VERSION.deb?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fsubsonic%2Ffiles%2Fsubsonic%2F$SUBSONIC_VERSION%2F&ts=1421842428&use_mirror=optimate
/tmp/subsonic-$SUBSONIC_VERSION.deb  
RUN dpkg -i /tmp/subsonic-$SUBSONIC_VERSION.deb && rm -f /tmp/*.deb  
  
# Create hardlinks to the transcoding binaries.  
# This way we can mount a volume over /var/subsonic.  
# Apparently, Subsonic does not accept paths in the Transcoding settings.  
# If you mount a volume over /var/subsonic, create symlinks  
# <host-dir>/var/subsonic/transcode/ffmpeg -> /usr/local/bin/ffmpeg  
# <host-dir>/var/subsonic/transcode/lame -> /usr/local/bin/lame  
RUN ln /var/subsonic/transcode/ffmpeg /var/subsonic/transcode/lame
/usr/local/bin && mkdir /mnt/music  
  
VOLUME /var/subsonic  
  
COPY startup.sh /startup.sh  
  
EXPOSE 4443  
CMD []  
ENTRYPOINT ["/startup.sh"]  
  

