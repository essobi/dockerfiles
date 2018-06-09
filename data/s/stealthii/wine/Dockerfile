FROM alpine:edge  
  
MAINTAINER Dan Porter "dpreid@gmail.com"  
RUN apk add --no-cache --virtual .wine-rundeps \  
wine \  
xvfb \  
&& winecfg  
  
RUN apk add --no-cache --virtual .winetricks \  
cabextract \  
unzip \  
p7zip \  
curl \  
wget \  
zenity \  
ncurses \  
&& curl -fSL
https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks
-o /usr/local/bin/winetricks \  
&& chmod +x /usr/local/bin/winetricks  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
ENV DISPLAY :0.0  
CMD ["wine64"]  

