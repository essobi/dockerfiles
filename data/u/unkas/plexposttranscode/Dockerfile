FROM unkas/lsio-ruby  
LABEL maintainer="Paul Snell"  
  
ENV GEM_VERSION 0.17.3  
  
RUN set -ex \  
&& apt-get update -qq && apt-get install -y --no-install-recommends software-
properties-common \  
&& add-apt-repository ppa:stebbins/handbrake-releases \  
&& apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
ffmpeg \  
mkvtoolnix \  
mp4v2-utils \  
mpv \  
handbrake-cli \  
&& apt-get remove -y software-properties-common && apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& gem install video_transcoding -v "$GEM_VERSION"  
  
ENV POSTDATA=/postproc  
ENV TVDIR=/media/TV \  
MVDIR=/media/Movies \  
POSTSCRIPTS="${POSTDATA}/bin" \  
QUEUEDIR="${POSTDATA}/queue" \  
QUEUEPROCESS=/usr/local/bin/plexTranscode \  
QUEUETIMER=600 \  
QUEUEDAYS=60 \  
REMOVETS=0 \  
TSCLEAN=1 \  
TSDAYS=60  
  
  
COPY root/ /  
  

