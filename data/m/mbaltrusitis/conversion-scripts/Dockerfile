FROM ubuntu:16.04  
MAINTAINER Matthew Baltrusitis <matthew@baltrusitis.com>  
  
ENV DEBIAN_FRONTEND="noninteractive"  
ENV SCRIPT_PATH /opt/conversion-scripts  
  
RUN apt-get -qy update && \  
apt-get install -qy software-properties-common && \  
add-apt-repository multiverse && \  
apt-get -qy update && \  
apt-get install -qy \  
ffmpeg \  
git \  
par2 \  
python-pip \  
vim && \  
pip install setuptools \  
requests \  
requests[security] \  
requests-cache \  
babelfish \  
guessit\<2 \  
subliminal\<2 \  
deluge-client \  
qtfaststart && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/* && \  
git clone https://github.com/mdhiggins/sickbeard_mp4_automator.git
"${SCRIPT_PATH}"  
  
ADD ["./autoProcess.ini.default", "/opt/conversion-scripts/autoProcess.ini"]  
  
VOLUME /opt/conversion-scripts  
  

