FROM ubuntu:16.04  
MAINTAINER Matthew Baltrusitis <matthew@baltrusitis.com>  
  
ENV DEBIAN_FRONTEND="noninteractive"  
ENV LANG "C"  
ENV HOME "/opt/sickbeard"  
ENV CONFIGS $HOME/.sickbeard  
  
RUN mkdir -p "${HOME}" \  
&& apt-get -qy update \  
&& apt-get install -qy --fix-missing \  
git \  
python-cheetah \  
python-openssl \  
&& git clone https://github.com/midgetspy/Sick-Beard.git "${HOME}"  
  
EXPOSE 8081  
VOLUME ["${CONFIGS}"]  
  
CMD ["python", "opt/sickbeard/SickBeard.py", "--
datadir=/opt/sickbeard/.sickbeard"]  
  

