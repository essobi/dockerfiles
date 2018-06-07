FROM steeb/cs16-amxmodx-32  
MAINTAINER Stefan Ebert <stefan-docker@ebert.li>  
  
WORKDIR /steam/cs16/cstrike  
RUN wget -O /tmp/gg.zip
"http://www.avalanche.gungame.org/files/download.php?file=v213c/gg_213c_full.zip"
&& unzip /tmp/gg.zip; rm /tmp/gg.zip  
RUN echo "gungame.amxx" > addons/amxmodx/configs/plugins.ini  
WORKDIR /steam/cs16/  

