FROM silverbulleters/vanessa-32bit-baseimage  
MAINTAINER "Shenja Sosna" <shenja@sosna.zp.ua>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN linux32 apt-get update && linux32 apt-get install -y -qq ngrok-client wget
curl zip unzip tar mono-runtime mono-mcs git-core \  
x11vnc vnc4server xvfb supervisor novnc ttf-ubuntu-font-family
libwebkitgtk-1.0-0 xfonts-cyrillic fluxbox software-properties-common \  
imagemagick libfreetype6 libgsf-bin libodbc1  
  
RUN linux32 apt-get install -y -qq --no-install-recommends wine \  
&& apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget -q --continue -O /tmp/oscript.zip http://oscript.io/downloads/night-
build/zip \  
&& unzip -o -q /tmp/oscript.zip -x "lib/*" -d /opt/oscript \  
&& git clone -b develop https://github.com/EvilBeaver/oscript-library.git
/opt/oscript/oscript-library \  
&& ln -s /opt/oscript/oscript-library/src/ /opt/oscript/lib \  
&& chmod +x /opt/oscript/bin/oscript.exe  

