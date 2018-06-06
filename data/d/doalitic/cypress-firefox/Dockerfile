FROM doalitic/cypress-base:8  
LABEL maintainer="Moss team <devops@moss.sh>"  
  
USER root  
  
# install Firefox - latest stable version  
ARG FIREFOX_VERSION=59.0.2  
RUN wget --no-verbose -O /tmp/firefox.tar.bz2 \  
https://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 \  
&& tar -C /opt -xjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& ln -fs /opt/firefox/firefox /usr/bin/firefox  

