#
-----------------------------------------------------------------------------  
# docker-yavdr-headless  
#  
#  
# Based on: Dominik Bücker  
# Updated: 16.09.2014  
# Require: Docker (http://www.docker.io/)  
#
-----------------------------------------------------------------------------  
FROM phusion/baseimage:0.9.13  
MAINTAINER jondalar <alex@iphonedation.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# don't ask for stupid things  
env DEBIAN_FRONTEND noninteractive  
RUN echo APT::Install-Recommends "0"; >> /etc/apt/apt.conf  
RUN echo APT::Install-Suggests "0"; >> /etc/apt/apt.conf  
  
#update the system  
RUN apt-get -y update && apt-get -y upgrade && dpkg-divert --local \--rename
--add /sbin/initctl && \  
ln -sf /bin/true /sbin/initctl  
  
# adding yavdr specific stuff  
run apt-add-repository -y ppa:yavdr/unstable-main  
run apt-add-repository -y ppa:yavdr/unstable-vdr  
run apt-add-repository -y ppa:yavdr/unstable-yavdr  
run apt-add-repository -y ppa:yavdr/unstable-xbmc  
  
# add mutiverse to sources.list to accomodate markad stuff  
RUN echo "deb http://security.ubuntu.com/ubuntu trusty multiverse" >>
/etc/apt/sources.list  
  
#update the system  
RUN apt-get -y update && apt-get -y upgrade  
  
# install vdr stuff  
RUN apt-get -y install at avahi-daemon bash-completion hsetroot logrotate
update-manager-core ureadahead vdr-plugin-dummydevice w-scan yavdr-essential-
docker-headless  
RUN apt-get -y install vlc-nox  
  
#maybe we have to add some of this. Just reordered to have a stable stub above
here, to reduce build time  
#RUN apt-get -y install acpid anacron at avahi-daemon bash-completion build-
essential cpufrequtils dvb-driver-sundtek-mediaclient ethtool ssh eventlircd
hsetroot i965-va-driver ir-keytable irserver libpam-ck-connector linux-
firmware linux-firmware-nonfree linux-firmware-yavdr lirc logrotate mhddfs
nvram-wakeup pm-utils ubuntu-extras-keyring udisks-glue update-manager-core
ureadahead usbutils vdr vdr-addon-acpiwakeup vdr-addon-avahi-linker vdr-addon-
lifeguard vdr-plugin-avahi4vdr vdr-plugin-channellists vdr-plugin-dbus2vdr
vdr-plugin-dummydevice vdr-plugin-dvbsddevice vdr-plugin-dvbhddevice vdr-
plugin-dynamite vdr-plugin-epgsearch vdr-plugin-femon vdr-plugin-live vdr-
plugin-markad vdr-plugin-menuorg vdr-plugin-pvr350 vdr-plugin-restfulapi vdr-
plugin-skinnopacity vdr-plugin-streamdev-server vdr-plugin-wirbelscan vdr-
skins-speciallogos vdr-tftng-anthraize vdr-tftng-pearlhd vdr-tftng-standard
vdr-xpmlogos vim wakeonlan wget wpasupplicant w-scan xfsprogs yavdr-base
yavdr-hostwakeup yavdr-remote yavdr-utils yavdr-webfrontend  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Expose Ports  
#EXPOSE 22  
EXPOSE 80  
EXPOSE 111  
EXPOSE 2004  
EXPOSE 2049  
EXPOSE 3000  
EXPOSE 6419  
EXPOSE 8002  
EXPOSE 8008  
#Stubs:  
#  
# add init/start  
# add Volume to link to for configs  
# use mkdir/ln -s/mv way to move generated configs to Volume  
# Guess:  
# /var/lib/vdr  
# /etc/vdr  
#add configfiles  
ADD ./vdrconfig/conf.d/ /etc/vdr/conf.d/  
ADD ./vdrconfig/conf.aval/ /etc/vdr/conf.aval/  
  
#Add runscript for vdr  
RUN mkdir /etc/service/vdr/  
ADD ./scripts/vdr/run /etc/service/vdr/run  
RUN chmod +x /etc/service/vdr/run  
  
#add runscript for tntnet / yavdr webinterface  
RUN mkdir /etc/service/tntnet/  
ADD ./scripts/tntnet/run /etc/service/tntnet/run  
RUN chmod +x /etc/service/tntnet/run  
  
#make a default user with name dockervdr and Password vdr  
RUN adduser --disabled-password --gecos "" dockervdr  
RUN echo "dockervdr:vdr"| chpasswd  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  

