FROM ubuntu:14.04  
MAINTAINER Pier Luigi Fiorini <pierluigi.fiorini@gmail.com>  
ADD public.key /  
ADD qt.list /etc/apt/sources.list.d/  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections && \  
echo keyboard-configuration keyboard-configuration/layout select 'English
(US)' | debconf-set-selections && \  
echo keyboard-configuration keyboard-configuration/layoutcode select 'us' |
debconf-set-selections && \  
echo "resolvconf resolvconf/linkify-resolvconf boolean false" | debconf-set-
selections && \  
apt-key add /public.key && \  
rm /public.key && \  
apt-get update && \  
apt-get install -y \  
ubuntu-minimal \  
curl \  
g++ \  
clang \  
xvfb \  
dbus \  
git \  
make \  
libfuse2 \  
pkg-config \  
cmake \  
libwayland-dev libwayland-egl1-mesa libegl1-mesa-dev \  
libfontconfig1-dev libglib2.0-dev libmtdev-dev libudev-dev \  
libxcomposite-dev libxkbcommon-dev libxrender-dev \  
qt510-meta-full  
# qbs >= 1.9.0 (which is what we need) doesn't build with gcc 4.8  
#ADD build-qbs.sh /  
#RUN /build-qbs.sh && rm -f /build-qbs.sh  
ADD build-qtwayland.sh /  
RUN /build-qtwayland.sh && rm -f /build-qtwayland.sh  
ADD entrypoint /usr/bin/docker-ubuntu-trusty-entrypoint  
  
ENTRYPOINT ["/usr/bin/docker-ubuntu-trusty-entrypoint"]  

