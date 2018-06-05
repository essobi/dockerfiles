FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get install -y wget git acl adwaita-icon-theme at-spi2-core colord colord-
data cpp cpp-5 dbus dbus-x11 dconf-gsettings-backend dconf-service desktop-
file-utils dh-python \  
dosfstools eject file fontconfig fontconfig-config fonts-dejavu-core fuse
gconf-service gconf-service-backend gconf2 gconf2-common gdisk glib-networking
glib-networking-common \  
glib-networking-services groff-base gsettings-desktop-schemas gvfs gvfs-bin
gvfs-common gvfs-daemons gvfs-libs hicolor-icon-theme humanity-icon-theme
libatasmart4 libatk-bridge2.0-0 \  
libatk1.0-0 libatk1.0-data libatspi2.0-0 libauthen-sasl-perl libavahi-client3
libavahi-common-data libavahi-common3 libboost-filesystem1.58.0 libboost-
system1.58.0 libcairo-gobject2 \  
libcairo2 libcap-ng0 libcolord2 libcolorhug2 libcroco3 libcups2 libdatrie1
libdbus-1-3 libdbus-glib-1-2 libdconf1 libdrm-amdgpu1 libdrm-intel1 libdrm-
nouveau2 libdrm-radeon1 libdrm2 \  
libegl1-mesa libelf1 libencode-locale-perl libepoxy0 libexif12 libfile-
basedir-perl libfile-desktopentry-perl libfile-listing-perl libfile-mimeinfo-
perl libfont-afm-perl libfontconfig1 \  
libfontenc1 libfreetype6 libfuse2 libgbm1 libgck-1-0 libgconf-2-4
libgcr-3-common libgcr-base-3-1 libgd3 libgdk-pixbuf2.0-0 libgdk-
pixbuf2.0-common libgl1-mesa-dri libgl1-mesa-glx \  
libglapi-mesa libglib2.0-0 libglib2.0-data libgphoto2-6 libgphoto2-l10n
libgphoto2-port12 libgraphite2-3 libgtk-3-0 libgtk-3-bin libgtk-3-common
libgtk2.0-0 libgtk2.0-bin libgtk2.0-common \  
libgudev-1.0-0 libgusb2 libharfbuzz0b libhtml-form-perl libhtml-format-perl
libhtml-parser-perl libhtml-tagset-perl libhtml-tree-perl libhttp-cookies-perl
libhttp-daemon-perl libhttp-date-perl \  
libhttp-message-perl libhttp-negotiate-perl libice6 libicu55 libieee1284-3
libio-html-perl libio-socket-ssl-perl libipc-system-simple-perl libisl15
libjbig0 libjpeg-turbo8 libjpeg8 \  
libjson-glib-1.0-0 libjson-glib-1.0-common liblcms2-2 libllvm3.8 libltdl7
liblwp-mediatypes-perl liblwp-protocol-https-perl libmagic1 libmailtools-perl
libmirclient9 libmircommon5 libxkbfile1 \  
libmirprotobuf3 libmpc3 libmpdec2 libmpfr4 libnet-dbus-perl libnet-http-perl
libnet-smtp-ssl-perl libnet-ssleay-perl libnotify4 libnspr4 libnss3
libnss3-nssdb libpam-systemd libpango-1.0-0 \  
libpangocairo-1.0-0 libpangoft2-1.0-0 libparted2 libpciaccess0 libpixman-1-0
libpng12-0 libpolkit-agent-1-0 libpolkit-backend-1-0 libpolkit-gobject-1-0
libprotobuf-lite9v5 libproxy1v5 \  
libpython-stdlib libpython2.7-minimal libpython2.7-stdlib libpython3-stdlib
libpython3.5-minimal libpython3.5-stdlib librest-0.7-0 librsvg2-2
librsvg2-common libsane libsane-common \  
libsecret-1-0 libsecret-common libsm6 libsoup-gnome2.4-1 libsoup2.4-1 libtext-
iconv-perl libthai-data libthai0 libtie-ixhash-perl libtiff5 libtimedate-perl
libtxc-dxtn-s2tc0 libudisks2-0 \  
liburi-perl libusb-1.0-0 libvpx3 libwayland-client0 libwayland-cursor0
libwayland-egl1-mesa libwayland-server0 libwww-perl libwww-robotrules-perl
libx11-protocol-perl libx11-xcb1 libxaw7 \  
libxcb-dri2-0 libxcb-dri3-0 libxcb-glx0 libxcb-present0 libxcb-render0 libxcb-
shape0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxcomposite1 libxcursor1
libxdamage1 libxfixes3 libxft2 libxi6 \  
libxinerama1 libxkbcommon0 libxml-parser-perl libxml-twig-perl libxml-
xpathengine-perl libxml2 libxmu6 libxpm4 libxrandr2 libxrender1 libxshmfence1
libxt6 libxtst6 libxv1 libxxf86dga1 \  
libxxf86vm1 mime-support notification-daemon ntfs-3g parted policykit-1 psmisc
python python-minimal python2.7 python2.7-minimal python3 python3-minimal
python3.5 python3.5-minimal sgml-base \  
shared-mime-info ubuntu-mono ucf udev udisks2 x11-common x11-utils
x11-xserver-utils xdg-user-dirs xdg-utils xkb-data xml-core nodejs systemd
libuv1 libudev1 libsystemd0 libxss1 libasound2 && \  
wget -O /tmp/atom-beta.deb "https://atom.io/download/deb?channel=beta" && dpkg
-i /tmp/atom-beta.deb && \  
apt-get clean && rm /tmp/atom-beta.deb && useradd -d /home/atom -m atom  
  
USER atom  
  
CMD [ "atom-beta", "-f" ]  

