FROM ubuntu:16.04  
  
MAINTAINER Michael Vierling  
  
ENV DEBCONF_NONINTERACTIVE_SEEN=true \  
DEBIAN_FRONTEND=noninteractive \  
KEY_SERVER=hkp://p80.pool.sks-keyservers.net:80 \  
VERSION_GOSU=1.10  
  
# Set default language to satisfy (debconf) xorg.  
RUN locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8  
  
RUN apt-get \--quiet --quiet update \  
&& apt-get \--quiet --quiet --no-install-recommends upgrade \  
&& apt-get \--quiet --assume-yes --no-install-recommends install \  
apt-utils \  
# ca-certificates come with curl  
curl \  
dirmngr \  
software-properties-common \  
unzip \  
vim \  
xz-utils  
  
RUN apt-get \--quiet update \  
&& apt-get \--quiet --assume-yes --no-install-recommends install \  
dbus-x11 \  
language-pack-gnome-en \  
# audio  
# Advanced Linux Sound Architecture  
alsa-base \  
alsa-oss \  
alsa-tools \  
alsa-utils \  
# GStreamer: open source multimedia framework  
gstreamer1.0 \  
# simple abstract interface for playing event sounds  
libcanberra0 \  
# translates GTK+ widgets signals to event sounds  
libcanberra-gtk3-dev \  
libcanberra-gtk3-module \  
libcanberra-gtk-module \  
# GStreamer backend for libcanberra  
libcanberra-gstreamer \  
# PulseAudio backend for libcanberra  
libcanberra-pulse \  
# video  
# Fonts with the same metrics as Times, Arial and Courier  
fonts-liberation \  
# Layout and rendering of internationalized text  
libpango1.0 \  
# Light Themes (Ambiance and Radiance)  
light-themes \  
# desktop integration utilities from freedesktop.org  
xdg-utils \  
# X.Org X server \-- output driver metapackage (installs opengl as dependency)  
xserver-xorg-video-all  
  
ENV GIMP_VERSION=2.8 \  
USER_PICTURES=/var/lib/gimp/pictures  
  
RUN add-apt-repository --yes ppa:otto-kesselgulasch/gimp \  
&& apt-get install --quiet --yes --no-install-recommends \  
# FIXME: install gimp 2.8 explicitely since ps relies on it  
gimp \  
gimp-ufraw \  
gimp-help-en \  
gimp-gap \  
gimp-gutenprint  
  
WORKDIR /etc/skel  
RUN ln --symbolic "${USER_PICTURES}" Pictures  
  
# Added to make GIMP look like PS.  
# WORKDIR /var/lig/gimp  
# RUN curl --fail --location --remote-name --show-error --silent
https://github.com/doctormo/GimpPs/archive/master.zip \  
# && unzip master.zip \  
# && rm master.zip \  
# && mv GimpPs-master "/etc/skel/.gimp-${GIMP_VERSION}"  
  
VOLUME ["${USER_PICTURES}"]  
  
# FIXME: Remember settings  
# VOLUME ["${USER_CONFIG}"]  
  
WORKDIR "${USER_PICTURES}"  
# ENTRYPOINT ["/entrypoint.sh", "gimp"]  
ENTRYPOINT ["gimp"]  
CMD ["--help"]  

