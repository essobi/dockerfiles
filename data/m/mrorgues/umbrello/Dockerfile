FROM debian:stretch-slim  
LABEL github "https://github.com/mrorgues"  
#============================#  
# Information & Requirements #  
#============================#  
# *** Run umbrello in a container ***  
#  
# docker run --rm -it \  
# --net host \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# -v $HOME/Documents:/root/Documents:rw \  
# -v $HOME/.config/umbrello:/root/.config:rw \  
# --name umbrello \  
# mrorgues/umbrello  
#===================#  
# Basics & Umbrello #  
#===================#  
RUN apt-get update && \  
apt-get install -y \  
ca-certificates \  
dbus-x11 \  
kinit \  
kio \  
libc6 \  
libgcc1 \  
libkf5archive5 \  
libkf5completion5 \  
libkf5configcore5 \  
libkf5configgui5 \  
libkf5configwidgets5 \  
libkf5coreaddons5 \  
libkf5i18n5 \  
libkf5iconthemes5 \  
libkf5jobwidgets5 \  
libkf5kiocore5 \  
libkf5kiowidgets5 \  
libkf5texteditor5 \  
libkf5textwidgets5 \  
libkf5widgetsaddons5 \  
libkf5xmlgui5 \  
libqt5core5a \  
libqt5gui5 \  
libqt5printsupport5 \  
libqt5svg5 \  
libqt5widgets5 \  
libqt5xml5 \  
libstdc++6 \  
libxml2 \  
libxslt1.1 \  
umbrello \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
  
#=============#  
# Here we go! #  
#=============#  
ENTRYPOINT ["/usr/bin/umbrello"]  

