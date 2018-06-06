# docker-kodi-server  
#  
# Setup: Clone repo then checkout appropriate version  
# For jarvis  
# $ git checkout jarvis  
# For Master (Lastest Kodi stable release)  
# $ git checkout master  
#  
# Create your own Build:  
# $ docker build --rm=true -t $(whoami)/kodi-server .  
#  
# Run your build:  
# $ docker run -d --restart="always" --net=host -v
/directory/with/kodidata:/opt/kodi-server/share/kodi/portable_data
$(whoami)/kodi-server  
#  
#  
# Greatly inspire by the work of wernerb,  
# See https://github.com/wernerb/docker-xbmc-server  
  
from base/archlinux  
maintainer celedhrim "celed+git@ielf.org"  
# Add headless patch  
ADD src/headless.patch /headless.patch  
# Install dep , compile , clean  
  
RUN cd /root && \  
pacman -Syu \--noprogressbar \--noconfirm && \  
pacman \--noprogressbar \--noconfirm -S git make autoconf automake pkg-config
swig jre8-openjdk-headless gcc python2 mesa-libgl glu libmariadbclient libass
tinyxml yajl libxslt taglib libmicrohttpd libxrandr libssh smbclient libnfs
ffmpeg libx264 cmake gperf unzip zip libcdio gtk-update-icon-cache rsync grep
sed gettext which && \  
ln -s /usr/bin/python2 /usr/bin/python && \  
ln -s /usr/bin/python2-config /usr/bin/python-config && \  
git clone https://github.com/xbmc/xbmc.git -b 17.6-Krypton \--depth=1 && \  
cd /root/xbmc && \  
make -C tools/depends/target/crossguid PREFIX=/usr/local && \  
make -C tools/depends/native/JsonSchemaBuilder/ && \  
cp tools/depends/native/JsonSchemaBuilder/bin/JsonSchemaBuilder /usr/local/bin
&& \  
chmod 775 /usr/local/bin/JsonSchemaBuilder && \  
mv /headless.patch . && \  
git apply headless.patch && \  
./bootstrap && \  
./configure \  
\--enable-nfs \  
\--enable-upnp \  
\--enable-ssh \  
\--with-ffmpeg=shared \  
\--disable-libbluray \  
\--disable-debug \  
\--disable-vdpau \  
\--disable-vaapi \  
\--disable-crystalhd \  
\--disable-vdadecoder \  
\--disable-vtbdecoder \  
\--disable-openmax \  
\--disable-joystick \  
\--disable-rsxs \  
\--disable-projectm \  
\--disable-rtmp \  
\--disable-airplay \  
\--disable-airtunes \  
\--disable-dvdcss \  
\--disable-optical-drive \  
\--disable-libusb \  
\--disable-libcec \  
\--disable-libmp3lame \  
\--disable-libcap \  
\--disable-udev \  
\--disable-libvorbisenc \  
\--disable-asap-codec \  
\--disable-afpclient \  
\--disable-goom \  
\--disable-fishbmc \  
\--disable-spectrum \  
\--disable-waveform \  
\--disable-avahi \  
\--disable-texturepacker \  
\--disable-pulse \  
\--disable-dbus \  
\--disable-alsa \  
\--disable-hal \  
\--prefix=/opt/kodi-server && \  
make && \  
make install && \  
mkdir -p /opt/kodi-server/share/kodi/portable_data/ && \  
cd /root && \  
mkdir empty && \  
rsync -a \--delete empty/ xbmc/ && \  
pacman \--noconfirm -Rnsc git make autoconf automake pkg-config swig
jre8-openjdk-headless gcc cmake gperf rsync gtk-update-icon-cache grep sed
gettext which && \  
rm -rf /root/* /usr/lib/python2.7/test /usr/share/doc /usr/share/man
/var/cache/pacman/pkg  
#Eventserver and webserver respectively.  
EXPOSE 9777/udp 8089/tcp  
CMD ["/opt/kodi-server/lib/kodi/kodi.bin","--headless","--no-test","--
nolirc","-p"]  

