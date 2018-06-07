FROM binhex/arch-delugevpn  
MAINTAINER ullbergm  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="Deluge" \  
org.label-schema.description="Deluge container with dependencies for
sickbeard_mp4_automator" \  
org.label-schema.url="http://ullberg.us/docker/deluge" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/ullbergm/docker-deluge" \  
org.label-schema.vendor="Magnus Ullberg" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
# install compiled packages using pacman  
RUN pacman -S --noconfirm --needed ffmpeg python2-pip && \  
pip2 install requests && \  
pip2 install requests[security] && \  
pip2 install requests-cache && \  
pip2 install babelfish && \  
pip2 install "guessit<2" && \  
pip2 install deluge-client && \  
pip2 install gevent && \  
pip2 install qtfaststart && \  
pip2 install "subliminal<2" && \  
pip2 install stevedore==1.19.1  

