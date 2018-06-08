#  
# docker run -d \  
# -v $HOME/Music:/home/mpd/music \  
# -v /tmp/mpd:/tmp/mpd \  
# -p 6600:6600 \  
# --device /dev/snd \  
# --name mpd \  
# germangb/mpd "$@"  
#  
FROM ubuntu:trusty  
MAINTAINER germangb <germangb42@gmail.com>  
  
# audio group id  
ARG gid=92  
RUN apt-get update \  
&& apt-get install -y mpd \  
&& rm -rf /var/lib/apt/lists  
  
# audio group with gid matching the host  
RUN groupmod -g ${gid} audio  
  
RUN mkdir /home/mpd && chown mpd /home/mpd  
  
COPY mpd.sh /usr/local/bin/mpd.sh  
RUN chmod +x /usr/local/bin/mpd.sh  
  
USER mpd  
  
ENV HOME=/home/mpd  
  
RUN mkdir -p /home/mpd/playlists && \  
mkdir -p /tmp/mpd && \  
mkdir -p /home/mpd/music && \  
touch /home/mpd/state && \  
touch /home/mpd/tag_cache  
  
COPY mpd.conf /home/mpd/mpd.conf  
  
ENTRYPOINT ["/usr/local/bin/mpd.sh"]  

