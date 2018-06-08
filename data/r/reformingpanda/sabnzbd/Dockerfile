FROM linuxserver/sabnzbd:latest  
RUN apt-get update && apt-get install git ffmpeg python-pip -y  
RUN pip install requests requests[security] requests-cache babelfish
"guessit<2" "subliminal<2" stevedore==1.19.1 python-dateutil qtfaststart  
RUN apt-get autoremove -y && \  
apt-get clean && \  
rm -rf \  
/tmp/* \  
/var/lib/apt/lists/* \  
/var/tmp/*  

