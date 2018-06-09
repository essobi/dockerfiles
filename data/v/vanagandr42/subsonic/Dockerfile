FROM vanagandr42/baseimage-oraclejdk:5  
# Package version  
ARG SUBSONIC_VER="6.1.3"  
# Environment settings  
ARG DEBIAN_FRONTEND="noninteractive"  
RUN BUILD_PACKAGES="" \  
&& apt-get update \  
&& apt-get install -y $BUILD_PACKAGES lame flac ffmpeg libavcodec-extra --no-
install-recommends \  
  
&& curl -o /tmp/subsonic-$SUBSONIC_VER.deb \  
https://s3-eu-west-1.amazonaws.com/subsonic-
public/download/subsonic-$SUBSONIC_VER.deb \  
&& dpkg -i /tmp/subsonic-$SUBSONIC_VER.deb \  
&& mkdir -p /music \  
  
# Cleanup  
# && apt-get purge -y --auto-remove $BUILD_PACKAGES \  
&& rm -rf /var/lib/apt/lists/* \  
/tmp/*  
  
# Declare volumes  
VOLUME ["/app", \  
"/playlists"]  
  
# Add local files  
COPY rootfs/ /  

