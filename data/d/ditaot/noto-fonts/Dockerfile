FROM java:8  
MAINTAINER Eliot Kimber "ekimber@contrext.com"  
# Container for the Google open-source noto fonts with an FOP configuration
file  
# to make them easy to use.  
WORKDIR /usr/share/fonts/opentype/noto  
RUN wget -O Noto-unhinted.zip -c https://noto-
website.storage.googleapis.com/pkgs/Noto-unhinted.zip && \  
unzip Noto-unhinted.zip && \  
rm Noto-unhinted.zip  
COPY fop /opt/fop  
VOLUME /usr/share/fonts  
VOLUME /opt/fop  
#  
# End of Docker file  
#

