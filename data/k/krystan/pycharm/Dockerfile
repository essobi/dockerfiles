FROM node:8.9.4-stretch  
LABEL maintainer "Krystan Honour <krystan@gmail.com>"  
  
# docker run -it \  
# --net host \  
# --cpuset-cpus 0 \  
# --memory 1500mb \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# --security-opt seccomp=$HOME/pycharm.json \  
# --device /dev/snd \  
# --device /dev/dri \  
# -v /dev/shm:/dev/shm \  
# -v $HOME/.pycharmhome:/home/pycharm \  
# --name pycharm \  
# --rm \  
# krystan/pycharm  
# Install pycharm  
WORKDIR /opt/pycharm  
  
ARG PYCHARMVERSION=pycharm-professional-2017.3.2  
ENV DISPLAY=unix$DISPLAY  
  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
libcanberra-gtk-module \  
curl \  
git-core \  
libsecret-1-0 gnome-keyring \  
gnupg \  
hicolor-icon-theme \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libpango1.0-0 \  
libpulse0 \  
libv4l-0 \  
fonts-symbola \  
\--no-install-recommends  
  
RUN apt-get install -y python python3-software-properties  
  
RUN curl -sSL -O
https://download.jetbrains.com/python/${PYCHARMVERSION}.tar.gz \  
&& mkdir pycharm \  
&& tar -xzvf ${PYCHARMVERSION}.tar.gz -C ./pycharm/ \  
\--strip-components=1 \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  
  
RUN groupadd -g 999 pycharm \  
&& useradd -r -u 999 -g pycharm -G audio,video pycharm \  
&& mkdir -p /home/pycharm \  
&& chown -R pycharm:pycharm /home/pycharm \  
&& chown -R pycharm:pycharm /opt/pycharm  
  
RUN npm install -g --unsafe-perm @angular/cli create-react-app react-scripts
react-cli react-native-cli react  
  
# Run pycharm as non privileged user  
USER pycharm  
  
# Autorun pycharm  
CMD [ "./pycharm/bin/pycharm.sh" ]  

