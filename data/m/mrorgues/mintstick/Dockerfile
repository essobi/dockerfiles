FROM debian:stretch-slim  
LABEL github "https://github.com/mrorgues"  
#============================#  
# Information & Requirements #  
#============================#  
# *** Run mintstick in a container ***  
# (USB Image Writer)  
#  
# docker run --rm -it \  
# -v $HOME/iso/:$HOME/ \  
# -v /etc/machine-id:/etc/machine-id \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# -v /var/run:/var/run \  
# -v /dev/bus/usb:/dev/bus/usb \  
# --privileged \  
# --net host \  
# --name mintstick \  
# mrorgues/mintstick  
#========#  
# Basics #  
#========#  
RUN apt-get update && \  
apt-get install -y \  
coreutils \  
dbus-x11 \  
gir1.2-glib-2.0 \  
gir1.2-gtk-3.0 \  
gir1.2-polkit-1.0 \  
libcanberra-gtk3-module \  
ntfs-3g \  
parted \  
policykit-1 \  
procps \  
python \  
python-dbus \  
python-gi \  
python-gi-cairo \  
python-glade2 \  
python-parted \  
gir1.2-udisks-2.0 \  
gir1.2-xapp-1.0 \  
udisks2 \  
util-linux \  
xdg-utils \  
\--no-install-recommends && \  
dbus-uuidgen --ensure=/etc/machine-id && \  
ln -sf /etc/machine-id /var/lib/dbus/machine-id && \  
rm -rf /var/lib/apt/lists/*  
  
  
#===========#  
# Mintstick #  
#===========#  
ENV VERSION 1.3.5  
ENV DOWNLOAD_URL
http://packages.linuxmint.com/pool/main/m/mintstick/mintstick_${VERSION}_all.deb  
RUN buildDeps='curl' && \  
set -x && \  
apt-get update && apt-get install -y $buildDeps --no-install-recommends && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sSL "${DOWNLOAD_URL}" > /tmp/mintstick_all.deb && \  
dpkg -i /tmp/mintstick_all.deb && \  
rm -rf /tmp/mintstick_all.deb && \  
apt-get purge -y --auto-remove $buildDeps  
  
  
#=============#  
# Here we go! #  
#=============#  
ENTRYPOINT ["/usr/bin/mintstick", "-m", "iso"]  

