FROM linuxserver/radarr  
MAINTAINER ullbergm  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Radarr" \  
org.label-schema.description="Radarr container with dependencies for
sickbeard_mp4_automator" \  
org.label-schema.url="http://ullberg.us/docker/radarr" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/ullbergm/docker-radarr" \  
org.label-schema.vendor="Magnus Ullberg" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
# install packages  
RUN \  
apt-get update && \  
apt-get install -y \  
\--no-install-recommends \  
\--no-install-suggests \  
ffmpeg \  
python-pip \  
python-dev \  
libffi-dev \  
libssl-dev \  
build-essential \  
gcc \  
binutils \  
git \  
cmake && \  
# install python modules  
pip install setuptools && \  
pip install wheel && \  
pip install requests && \  
pip install requests[security] && \  
pip install requests-cache && \  
pip install babelfish && \  
pip install "guessit<2" && \  
pip install deluge-client && \  
pip install qtfaststart && \  
pip install "subliminal<2" && \  
pip install stevedore==1.19.1 && \  
# remove build tools  
apt-get purge -y --auto-remove \  
build-essential && \  
# clean up  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  

