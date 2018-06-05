FROM debian:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
EXPOSE 5901  
  
ADD start.sh /start.sh  
  
RUN sed -e 's/deb/deb-src/' /etc/apt/sources.list >
/etc/apt/sources.list.d/debian-sources.list \  
&& apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install -y \  
adduser \  
apt-utils \  
ca-certificates \  
calendar-google-provider \  
command-not-found \  
dbus \  
devscripts \  
enigmail \  
fakeroot \  
firefox-esr \  
firefox-esr-l10n-nl \  
fonts-wqy-microhei \  
fonts-liberation \  
fuse \  
git-core \  
gnupg \  
lsb-release \  
less \  
libnspr4 \  
libnss3 \  
libappindicator1 \  
libcurl3 \  
lightning \  
mr \  
openssh-sftp-server \  
paprefs \  
patch \  
procps \  
pulseaudio \  
pulseaudio-utils \  
screen \  
secpanel \  
ssh \  
sshfs \  
sudo \  
supervisor \  
task-xfce-desktop \  
tightvncserver \  
tmux \  
thunderbird \  
thunderbird-l10n-nl \  
xul-ext-adblock-plus \  
xul-ext-dispmua \  
xul-ext-https-everywhere \  
xul-ext-livehttpheaders \  
xul-ext-timeline \  
xfce4 \  
xfce4-goodies \  
vcsh \  
vim \  
wget \  
&& apt-get -y install --no-install-recommends `apt-cache search xfce | cut -d
' ' -f1` \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN mkdir -p /var/run/dbus /var/run/sshd /etc/xdg/xfce4/xfconf/xfce-
prechannel-xml \  
&& chown messagebus:messagebus /var/run/dbus \  
&& chmod 0755 /var/run/sshd \  
&& dbus-uuidgen --ensure \  
&& echo "[supervisord]\nnodaemon=true\n" >
/etc/supervisor/conf.d/supervisord.conf \  
&& echo "[program:dbus-daemon]\ncommand=/usr/bin/dbus-daemon --system
--nofork\nuser=messagebus\n" >> /etc/supervisor/conf.d/supervisord.conf \  
&& echo "[program:vncserver]\ncommand=/usr/bin/vncserver -depth 24 -geometry
1440x900 -rfbauth /home/user/.vnc/passwd
:1\nUSER=user\nenvironment=DISPLAY=:1,HOME=/home/user/,USER=user\nautorestart=true\n"
>> /etc/supervisor/conf.d/supervisord.conf \  
&& echo "[program:sshd]\ncommand=/usr/sbin/sshd -D\n" >>
/etc/supervisor/conf.d/supervisord.conf \  
&& echo "load-module module-native-protocol-tcp auth-anonymous=1" >>
/etc/pulse/default.pa \  
# && mv /etc/xdg/xfce4/panel/default.xml /etc/xdg/xfce4/xfconf/xfce-
prechannel-xml/xfce4-panel.xml \  
&& rm /etc/xdg/autostart/xscreensaver.desktop \  
&& chmod +x /start.sh  
  
CMD ["/start.sh" ]  

