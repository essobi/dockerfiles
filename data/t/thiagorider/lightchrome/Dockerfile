# Run a light Chrome in a container  
#  
# docker run -it \  
# \--net host \  
# \--cpuset-cpus 0 \ # control the cpu  
# \--memory 512mb \ # max memory it can use  
# -v /tmp/.X11-unix:/tmp/.X11-unix \ # mount the X11 socket  
# -e DISPLAY=$DISPLAY \  
# -v $HOME/Downloads:/root/Downloads \  
# -v $HOME/.config/google-chrome/:/data \ # if you want to save state  
# \--device /dev/snd \ # so we have sound  
# -v /dev/shm:/dev/shm \  
# \--name chrome \  
# thiagorider/lightchrome  
#  
#  
#  
#  
  
# Base docker image  
FROM alpine  
MAINTAINER Thiago Rider Augusto <thiago.rider@gmail.com>  
  
  
#ADD https://dl.google.com/linux/direct/google-talkplugin_current_amd64.deb
/src/google-talkplugin_current_amd64.deb  
  
#ADD https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
/src/google-chrome-stable_current_amd64.deb  
  
# Install Chrome  
RUN apk add --update --no-cache \  
bash \  
chromium \  
chromium-doc \  
ca-certificates \  
# fonts-liberation \  
# fonts-roboto \  
# gconf-service \  
hicolor-icon-theme \  
# libappindicator1 \  
# libasound2 \  
# libcanberra-gtk-module \  
# libcurl3 \  
libexif-dev \  
# libfontconfig1 \  
# libfreetype6 \  
# libgconf-2-4 \  
# libgl1-mesa-dri \  
# libgl1-mesa-glx \  
# libnspr4 \  
# libnss3 \  
pango \  
v4l-utils-libs \  
# libxss1 \  
# libxtst6 \  
# lsb-base \  
strace \  
wget \  
xdg-utils  
# fonts-symbola \  
# apk -i '/src/google-chrome-stable_current_amd64.deb' && \  
# && rm -rf /var/cache/apk/*  
  
# Set chrome as the process started  
ENTRYPOINT [ "chromium-browser" ]  
CMD [ "--user-data-dir=/data" ]  

