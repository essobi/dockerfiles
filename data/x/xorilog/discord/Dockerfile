# Base docker image  
FROM debian:jessie  
LABEL maintainer "Christophe Boucharlat <christophe.boucharlat@gmail.com>"  
# Discord Version 0.0.4  
  
RUN apt-get update && apt-get install -y \  
apt-utils \  
dbus-x11 \  
dunst \  
hunspell-en-us \  
python3-dbus \  
software-properties-common \  
libx11-xcb1 \  
gconf2 \  
libgtk2.0-0 \  
libxtst6 \  
libnss3 \  
libasound2 \  
wget \  
\--no-install-recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget https://dl.discordapp.net/apps/linux/0.0.4/discord-0.0.4.tar.gz -O
/tmp/discord.tar.gz && \  
cd /tmp/ && \  
tar xvzf /tmp/discord.tar.gz && \  
rm /etc/fonts/conf.d/10-scale-bitmap-fonts.conf && \  
fc-cache -fv  
  
ENV QT_XKB_CONFIG_ROOT=/usr/share/X11/xkb  
  
## Autorun Discord  
CMD ["/tmp/Discord/Discord"]  

