# Rocrail image  
#  
#
------------------------------------------------------------------------------  
# NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"  
#  
# PLEASE DO NOT EDIT IT DIRECTLY.  
#
------------------------------------------------------------------------------  
#  
FROM multiarch/debian-debootstrap:armhf-stretch  
  
# Set download urls  
ENV DEBIAN_FRONTEND="noninteractive"
ROCRAIL_URL="https://launchpad.net/rocrail/sunrise/2.0/+download/rocrail-12957-stretch-
wx3.0-armhf.deb"  
# Add universe source for amd64 bit to install libwxgtk3.0-dev in ubuntu and
install rocrail  
RUN echo "deb [arch=amd64] http://archive.ubuntu.com/ubuntu/ xenial universe"
| tee -a /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends -y \  
ca-certificates \  
libusb-1.0-0-dev \  
libwxgtk3.0-dev \  
unzip \  
wget \  
&& wget -nv -O /tmp/rocrail.deb ${ROCRAIL_URL} \  
&& dpkg --install --force-depends /tmp/rocrail.deb \  
&& mkdir /opt/rocrail/settings \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Start this container  
VOLUME [ "/opt/rocrail/settings" ]  
EXPOSE 8051  
WORKDIR /opt/rocrail  
CMD [ "./rocrail", "-nodevcheck", "-w", "/opt/rocrail/settings", "-l",
"/opt/rocrail" ]  

