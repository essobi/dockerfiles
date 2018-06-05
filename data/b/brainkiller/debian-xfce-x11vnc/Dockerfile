FROM debian:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
ARG user=user  
ARG group=user  
ARG uid=2000  
ARG gid=2000  
  
EXPOSE 5900  
  
ADD start.sh /start.sh  
  
RUN sed -e 's/deb/deb-src/' /etc/apt/sources.list >
/etc/apt/sources.list.d/debian-sources.list \  
&& apt-get update \  
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
tmux \  
thunderbird \  
thunderbird-l10n-nl \  
x11vnc \  
xul-ext-adblock-plus \  
xul-ext-dispmua \  
xul-ext-https-everywhere \  
xul-ext-livehttpheaders \  
xul-ext-timeline \  
xfce4 \  
xfce4-goodies \  
xvfb \  
vcsh \  
vim \  
wget \  
&& apt-get -y install --no-install-recommends `apt-cache search xfce | cut -d
' ' -f1` \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# add our user and group first to make sure their IDs get assigned
consistently, regardless of whatever dependencies get added  
RUN groupadd -g ${gid} ${group} \  
&& useradd -u ${uid} -g ${gid} -m -s /bin/bash -G sudo,audio ${user} \  
&& mkdir -p /var/run/dbus /var/run/sshd \  
&& chown messagebus:messagebus /var/run/dbus \  
&& chmod 0755 /var/run/sshd \  
&& dbus-uuidgen --ensure \  
&& echo "[supervisord]\nnodaemon=true\n" >
/etc/supervisor/conf.d/supervisord.conf \  
&& echo "[program:x11vnc]\ncommand=x11vnc -forever -usepw -noncache -rfbauth
/usr/local/etc/x11vnc.passwd -reopen -shared
-verbose\nenvironment=DISPLAY=:1\n" >> /etc/supervisor/conf.d/supervisord.conf
\  
&& echo "[program:Xvfb]\ncommand=/usr/bin/Xvfb :1 -screen 0 1440x900x24
+extension RANDR\n" >> /etc/supervisor/conf.d/supervisord.conf \  
&& echo "[program:dbus-daemon]\ncommand=/usr/bin/dbus-daemon --system
--nofork\nuser=messagebus\n" >> /etc/supervisor/conf.d/supervisord.conf \  
&& echo
"[program:xfce]\ncommand=/usr/bin/startxfce4\nuser=user\nenvironment=DISPLAY=:1,HOME=/home/user/\nautorestart=true\n"
>> /etc/supervisor/conf.d/supervisord.conf \  
&& echo "[program:sshd]\ncommand=/usr/sbin/sshd -D\n" >>
/etc/supervisor/conf.d/supervisord.conf \  
#&& echo "xset s" > /home/${user}/.xsession \  
&& echo "/usr/bin/startxfce4" > /home/${user}/.xsession \  
&& echo "load-module module-native-protocol-tcp auth-anonymous=1" >>
/etc/pulse/default.pa \  
&& rm /etc/xdg/autostart/xscreensaver.desktop \  
&& chmod +x /start.sh  
  
CMD ["/start.sh" ]  

