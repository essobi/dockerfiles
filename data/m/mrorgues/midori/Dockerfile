FROM debian:stretch-slim  
LABEL github "https://github.com/mrorgues"  
#============================#  
# Information & Requirements #  
#============================#  
# *** Run midori in a container ***  
#  
# docker run --rm -it \  
# --net host \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# --device /dev/dri \  
# --device /dev/snd \  
# -v /dev/shm:/dev/shm \  
# -v /etc/fonts:/etc/fonts \  
# -v /etc/machine-id:/etc/machine-id \  
# -v /usr/share/fonts:/usr/share/fonts \  
# -v $HOME/.config/midori:/root/.config/midori \  
# --ipc="host" \  
# --name midori \  
# mrorgues/midori  
#=================#  
# Basics & Midori #  
#=================#  
RUN apt-get update && \  
apt-get install -y \  
ca-certificates \  
dbus-x11 \  
gstreamer1.0-alsa \  
gstreamer1.0-libav \  
gstreamer1.0-plugins-good \  
libc6 \  
libcairo2 \  
libcanberra-gtk-module \  
libgdk-pixbuf2.0-0 \  
libglib2.0-0 \  
libgtk2.0-0 \  
libjavascriptcoregtk-1.0-0 \  
libnotify4 \  
libpango1.0-0 \  
libsoup2.4-1 \  
libsqlite3-0 \  
libunique-1.0-0 \  
libwebkitgtk-1.0-0 \  
libx11-6 \  
libxml2 \  
libxss1 \  
midori \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
  
#=============#  
# Here we go! #  
#=============#  
ENTRYPOINT [ "/usr/bin/midori" ]  

