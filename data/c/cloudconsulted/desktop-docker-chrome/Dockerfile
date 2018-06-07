# Docker 1.8  
# $ docker run -it \  
# \--net host \ # may as well YOLO  
# \--cpuset 0 \ # control the cpu  
# \--memory 512mb \ # max memory it can use  
# -v /tmp/.X11-unix:/tmp/.X11-unix \ # mount the X11 socket  
# -e DISPLAY=unix$DISPLAY \ # pass the display  
# -v $HOME/Downloads:/root/Downloads \ # optional, but nice  
# -v $HOME/.config/google-chrome/:/data \ # if you want to save state  
# \--device /dev/snd \ # so we have sound  
# \--name chrome \  
# cloudconsulted/desktop-docker-chrome  
#  
# Docker 1.7-prior  
# $ docker run -it \  
# \--net host \ # may as well YOLO  
# \--cpuset 0 \ # control the cpu  
# \--memory 512mb \ # max memory it can use  
# -v /tmp/.X11-unix:/tmp/.X11-unix \ # mount the X11 socket  
# -e DISPLAY=unix$DISPLAY \ # pass the display  
# -v $HOME/Downloads:/root/Downloads \ # optional, but nice  
# -v $HOME/.config/google-chrome/:/data \ # if you want to save state  
# -v /dev/snd:/dev/snd --privileged \ # so we have sound  
# \--name chrome \  
# cloudconsulted/desktop-docker-chrome  
  
# Base docker image  
FROM debian:sid  
MAINTAINER John Wooten/CONSULTED <jwooten@cloudconsulted.com>  
  
COPY google-talkplugin_current_amd64.deb /src/google-
talkplugin_current_amd64.deb  
  
ADD https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
/src/google-chrome-stable_current_amd64.deb  
  
# Install Chromium  
RUN mkdir -p /usr/share/icons/hicolor && \  
apt-get update && apt-get install -y \  
ca-certificates \  
gconf-service \  
hicolor-icon-theme \  
libappindicator1 \  
libasound2 \  
libcanberra-gtk-module \  
libcurl3 \  
libexif-dev \  
libgconf-2-4 \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libnspr4 \  
libnss3 \  
libpango1.0-0 \  
libv4l-0 \  
libxss1 \  
libxtst6 \  
wget \  
xdg-utils \  
\--no-install-recommends && \  
dpkg -i '/src/google-chrome-stable_current_amd64.deb' && \  
dpkg -i '/src/google-talkplugin_current_amd64.deb' \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY local.conf /etc/fonts/local.conf  
  
# Autorun chrome  
ENTRYPOINT [ "/usr/bin/google-chrome" ]  
CMD [ "--user-data-dir=/data", "--no-sandbox" ]  

