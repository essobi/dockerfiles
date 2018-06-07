FROM python:2.7  
MAINTAINER Victor Kulichenko <onclev@gmail.com>  
ARG PUID=1000  
ARG PGID=1000  
ENV VER=1.3.5  
COPY plex-scrobble /plex-scrobble  
RUN groupadd -g $PGID plex && useradd -m -g $PGID -u $PUID plex  
RUN wget -qO- https://github.com/jesseward/plex-lastfm-
scrobbler/archive/${VER}.tar.gz | tar -xzC /tmp \  
&& cd /tmp/plex-lastfm-scrobbler-${VER} \  
&& python setup.py install \  
&& cp /root/.config/plex-lastfm-scrobbler/plex_scrobble.conf / \  
&& rm -R /tmp/plex-lastfm-scrobbler-${VER} /root/.config/plex-lastfm-scrobbler
\  
&& mkdir -p /home/plex/.config/plex-lastfm-scrobbler \  
&& sed -i -e 's%/tmp/plex_scrobble.log%/home/plex/.config/plex-lastfm-
scrobbler/plex_scrobble.log%g' \  
-e 's%/path/to/plex/media/server/log%/config/Library/Application Support/Plex Media Server/Logs/Plex Media Server.log%g' /plex_scrobble.conf \  
&& chown plex:plex -R /home/plex/.config /plex_scrobble.conf \  
&& chmod +x /plex-scrobble  
COPY ./plex-scrobble.py /usr/local/bin/plex-scrobble.py  
USER plex  
VOLUME ["/home/plex/.config/plex-lastfm-scrobbler"]  
STOPSIGNAL SIGINT  
CMD ["/plex-scrobble"]  

