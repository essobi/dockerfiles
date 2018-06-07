FROM tianon/makemkv  
MAINTAINER William Weiskopf <william@weiskopf.me>  
  
ENV VIDEOTRANSCODE_VERSION 0.17.2  
# handbrake and mkvtoolnix are still in Alpines edge/testing  
RUN apt-get update && apt-get install -y \  
handbrake-cli \  
libav-tools \  
mkvtoolnix \  
mp4v2-utils \  
ruby \  
&& rm -rf /var/lib/apt/lists/*  
RUN gem install video_transcoding -v "$VIDEOTRANSCODE_VERSION"  
  
#USER root  
WORKDIR /media  
  
ENTRYPOINT []  
  
#CMD ["crond", "-l", "0", "-f"]  

