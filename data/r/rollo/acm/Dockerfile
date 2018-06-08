# Run Chrome in a container  
#  
# docker run -it \  
# \--net host \ # may as well YOLO  
# \--cpuset-cpus 0 \ # control the cpu  
# \--memory 512mb \ # max memory it can use  
# -v /tmp/.X11-unix:/tmp/.X11-unix \ # mount the X11 socket  
# -e DISPLAY=unix$DISPLAY \  
# -v $HOME/Downloads:/root/Downloads \  
# -v $HOME/.config/google-chrome/:/data \ # if you want to save state  
# \--device /dev/snd \ # so we have sound  
# -v /dev/shm:/dev/shm \  
# \--name chrome \  
# jess/chrome  
#  
# inspired by Jessie Frazelle <jess@linux.com>  
# https://github.com/jessfraz/dockerfiles/blob/master/chrome/stable/Dockerfile  
#  
# Usage: docker run --rm -it --net host --cpuset-cpus 0 --memory 512mb -e
DISPLAY=192.168.99.1:0 --name chrome rollo/mychrome  
# this construct requires a local X server and socket to host it (hint: socat
...)  
  
# Base docker image  
FROM ubuntu:17.04  
MAINTAINER rollo # that's me! ;-)  
  
# Uncomment this and in the install section if you want this plugin  
#ADD https://dl.google.com/linux/direct/google-talkplugin_current_amd64.deb
/src/google-talkplugin_current_amd64.deb  
  
# Install Chrome  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
fonts-symbola \  
gnupg \  
hicolor-icon-theme \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libpulse0 \  
libv4l-0 \  
\--no-install-recommends \  
&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
\  
&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main"
> /etc/apt/sources.list.d/google.list \  
&& apt-get update && apt-get install -y \  
google-chrome-stable \  
\--no-install-recommends \  
# && dpkg -i '/src/google-talkplugin_current_amd64.deb' \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  
  
# Create a runtime user  
RUN groupadd -r dev && useradd -m -r -g dev dev  
  
# Switch to the userspace  
USER dev  
ENV HOME /home/dev  
WORKDIR $HOME  
  
# Install saved configuration  
#COPY local.conf /etc/fonts/local.conf  
  
# Autorun chrome  
ENTRYPOINT [ "google-chrome" ]  
CMD [ "--user-data-dir=/data" ]  

