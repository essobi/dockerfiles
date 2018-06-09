FROM ubuntu:xenial  
MAINTAINER Daniel Yokomizo <daniel.yokomizo@gmail.com>  
  
RUN apt-get update \  
&& apt-get install --yes \  
libcairo2-dev \  
libglib2.0-0 \  
libgtk2.0-dev \  
libpango1.0-dev \  
libx11-6 \  
nano \  
wget  
  
COPY sublime-text_build-3126_amd64.deb.sha512 /opt/sublime-
text_build-3126_amd64.deb.sha512  
  
RUN wget --quiet --directory-prefix=/opt
https://download.sublimetext.com/sublime-text_build-3126_amd64.deb \  
&& sha512sum --check /opt/sublime-text_build-3126_amd64.deb.sha512 \  
&& dpkg --install /opt/sublime-text_build-3126_amd64.deb \  
&& rm /opt/sublime-text_build-3126_amd64.deb /opt/sublime-
text_build-3126_amd64.deb.sha512  
  
RUN echo '#!/bin/bash' > /opt/sublime \  
&& echo '/opt/sublime_text/sublime_text' >> /opt/sublime \  
&& chmod +x /opt/sublime  
  
CMD ["/opt/sublime"]  

