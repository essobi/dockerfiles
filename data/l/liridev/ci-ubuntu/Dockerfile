FROM ubuntu:16.04  
MAINTAINER Pier Luigi Fiorini <pierluigi.fiorini@gmail.com>  
ADD public.key /  
ADD neon.list /etc/apt/sources.list.d/  
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
qbs \  
pkg-config \  
cmake \  
libwayland-dev libwayland-egl1 libegl1-mesa-dev \  
libfontconfig1-dev libglib2.0-dev libinput-dev libmtdev-dev libudev-dev \  
libxcomposite-dev libxkbcommon-dev libxrender-dev \  
qt5-default \  
qtbase5-dev qtbase5-dev-tools qtbase5-private-dev \  
qtdeclarative5-dev qtdeclarative5-dev-tools qtdeclarative5-private-dev \  
qtquickcontrols2-5-dev \  
libqt5svg5-dev \  
qtwebengine5-dev qtwebengine5-dev-tools \  
qttools5-dev qttools5-dev-tools qttools5-private-dev \  
qml-module-qtquick2 qml-module-qtquick-window2 qml-module-qtquick-layouts qml-
module-qttest \  
qml-module-qtgraphicaleffects qml-module-qtqml-models2 \  
qml-module-qtquick-controls2 qml-module-qtquick-templates2 \  
qml-module-qt-labs-platform qml-module-qt-labs-calendar \  
qml-module-qt-labs-folderlistmodel qml-module-qt-labs-settings \  
qml-module-qt-labs-handlers qml-module-qt-labs-platform \  
qml-module-qt-labs-sharedimage \  
qml-module-qtwebengine qml-module-qtwebchannel  
ADD build-qtwayland.sh /  
RUN /build-qtwayland.sh && rm -f /build-qtwayland.sh  

