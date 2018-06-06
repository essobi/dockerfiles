# Run windows programs like a champion  
FROM ubuntu:14.04  
MAINTAINER benjamin.gemmill@gmail.com  
  
RUN apt-get update && apt-get install -y locales && locale-gen en_US.UTF-8  
ENV LANG='en_US.UTF-8' LC_ALL='en_US.UTF-8'  
RUN apt-get update && apt-get install -y \  
software-properties-common \  
&& add-apt-repository -y ppa:ubuntu-wine/ppa  
  
# versions for wine things here: https://launchpad.net/~ubuntu-
wine/+archive/ubuntu/ppa  
RUN dpkg --add-architecture i386  
RUN apt-get update && apt-get install -y \  
wine1.8 \  
wine-mono4.5.6 \  
wine-gecko2.40 \  
wine-gecko2.40:i386 \  
xvfb  
  
# Generate wine settings, waiting for wineserver to finish  
RUN xvfb-run wine "wineboot" && while pgrep -u `whoami` wineserver >
/dev/null; do sleep 1; done  
  
# For reference, generate wine settings for 32 bit windows in a custom
location  
#RUN WINEPREFIX="/root/.wine32" WINEARCH="win32" xvfb-run wine "wineboot"  
#CMD wine "/root/.wine/drive_c/Program Files/Internet Explorer/iexplore.exe"  
RUN apt-get purge -yq software-properties-common \  
&& apt-get autoremove -yq \  
&& apt-get autoclean -yq \  
&& rm -rf /var/lib/apt/lists/*  

