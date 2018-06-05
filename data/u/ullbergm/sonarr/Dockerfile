FROM linuxserver/sonarr  
MAINTAINER ullbergm  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Sonarr" \  
org.label-schema.description="Sonarr container with dependencies for
sickbeard_mp4_automator" \  
org.label-schema.url="http://ullberg.us/docker/sonarr" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/ullbergm/docker-sonarr" \  
org.label-schema.vendor="Magnus Ullberg" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
# install packages  
RUN \  
apt-get update && \  
apt-get install -y \  
ffmpeg \  
python-pip \  
python-dev \  
libffi-dev \  
libssl-dev \  
gcc \  
binutils \  
git \  
cmake && \  
pip install requests && \  
pip install requests[security] && \  
pip install requests-cache && \  
pip install babelfish && \  
pip install "guessit<2" && \  
pip install deluge-client && \  
pip install qtfaststart && \  
pip install "subliminal<2" && \  
pip install stevedore==1.19.1 && \  
  
rm -rf /tmp/* /var/lib/apt  
  

