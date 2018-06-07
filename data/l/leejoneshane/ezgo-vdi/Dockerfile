FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV SCRATCH_VERSION 456.0.4  
ENV TZ Asia/Taipei  
ADD servers.conf /etc/supervisor/conf.d/servers.conf  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends sudo vim-tiny wget git apt-
transport-https ca-certificates pulseaudio python-psutil locales apt-utils \  
&& addgroup chrome-remote-desktop \  
&& useradd -m -s /bin/bash -G sudo,chrome-remote-desktop,pulse-access ezgo \  
&& echo "ezgo:ezgo" | chpasswd \  
&& echo 'ezgo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \  
&& wget --no-check-certificate -O -
https://ezgo.goodhorse.idv.tw/apt/ezgo/ezgo.gpg.key | apt-key add \- \  
&& echo "deb https://ezgo.goodhorse.idv.tw/apt/ezgo/ ezgo13 main" >
/etc/apt/sources.list.d/ezgo.list \  
&& dpkg --add-architecture i386 \  
&& echo "zh_TW.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen "zh_TW.UTF-8" \  
&& dpkg-reconfigure locales \  
&& ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
\  
&& apt-get update && apt-mark hold bluez-obexd \  
&& apt-get install -y \  
net-tools openssh-server python-pip python-dev build-essential mesa-utils
x11vnc xvfb xrdp supervisor \  
kubuntu-desktop konsole libglib2.0-bin libappindicator1 gconf-service
libgconf-2-4 \  
language-pack-zh-hant language-pack-gnome-zh-hant firefox firefox-locale-zh-
hant libreoffice libreoffice-l10n-zh-tw \  
msttcorefonts ttf-ubuntu-font-family fonts-wqy-microhei fonts-liberation
icedtea-netx icedtea-plugin \  
qtqr gimp tuxpaint inkscape vlc filezilla audacity p7zip-full dia
furiusisomount klavaro ksnapshot ktuberling \  
about-ezgo ezgo-menu ezgo-kde ezgo-artwork ezgo-games xmind \  
ezgo-chem ezgo-tasks ezgo-education ezgo-graphics ezgo-gsyan ezgo-phet
ezgo-s4a ezgo-usgs \  
ezgo-misc-arduino-rules ezgo-misc-audacity ezgo-misc-decompress ezgo-misc-
desktop-files \  
ezgo-misc-furiusisomount ezgo-misc-inkscape ezgo-misc-installer \  
ezgo-misc-klavaro ezgo-misc-ksnapshot ezgo-misc-ktuberling ezgo-misc-qtqr
ezgo-misc-kdenlive \  
ezgo-misc-tuxpaint ezgo-npa ezgo-wordtest ubiquity-slideshow-ezgo \  
fcitx fcitx-chewing fcitx-libs-qt5 fcitx-table-array30-big fcitx-table-
cangjie3 \  
fcitx-tools fcitx-m17n ezgo-misc-fcitx-dayi3 policykit-1 xbase-clients \  
&& apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* \  
&& cd /root \  
&& wget -O chrome.deb https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& wget -O crd.deb https://dl.google.com/linux/direct/chrome-remote-
desktop_current_amd64.deb \  
&& dpkg -i ./chrome.deb && dpkg -i ./crd.deb && rm -f chrome.deb crd.deb \  
&& cd /usr/lib \  
&& git clone https://github.com/novnc/noVNC \  
&& cp /usr/lib/noVNC/vnc.html /usr/lib/noVNC/index.html \  
&& cd /usr/lib/noVNC/utils \  
&& git clone https://github.com/novnc/websockify \  
&& xrdp-keygen xrdp auto \  
&& mkdir -p /home/ezgo/.config/chrome-remote-desktop \  
&& echo startkde >> /home/ezgo/.xsession \  
&& chown -R ezgo:ezgo /home/ezgo \  
&& echo 'Acquire::ForceIPv4 "true";' > /etc/apt/apt.conf.d/99force-ipv4 \  
&& echo 'DPkg::Post-Invoke {"if [ -x /usr/share/ezgo/ezgo-menu/update-
desktop.sh ]; then sudo /usr/share/ezgo/ezgo-menu/update-desktop.sh; fi; ";};'
> /etc/apt/apt.conf.d/80update-ezgomenu \  
&& echo "1" | update-alternatives --config x-www-browser  
  
ADD google-chrome.desktop /usr/share/applications/google-chrome.desktop  
USER ezgo  
WORKDIR /home/ezgo  
  
ENV LANG zh_TW.UTF-8  
ENV LANGUAGE zh_TW.utf-8  
ENV LC_ALL zh_TW.UTF-8  
ENV DISPLAY :1  
  
EXPOSE 80 3389 5900  
CMD sudo /usr/bin/supervisord -n  

