FROM debian:jessie  
MAINTAINER antoniorossi <antoniorossi@outlook.com>  
  
# env to override for daemon user if needed  
ENV USER_NAME dropbox  
ENV USER_PASSWORD dropbox  
ENV GROUP_NAME $USER_NAME  
ENV USER_ID 1001  
ENV GROUP_ID 1001  
ENV HOME /dbox  
ENV NETATALK_VERSION 3.1.8  
# Copy build files  
COPY ./root /  
  
ENV DEPS="build-essential libevent-dev libssl-dev libgcrypt11-dev libkrb5-dev
libpam0g-dev libwrap0-dev libdb-dev libtdb-dev libmysqlclient-dev libavahi-
client-dev libacl1-dev libldap2-dev libcrack2-dev systemtap-sdt-dev
libdbus-1-dev libdbus-glib-1-dev libglib2.0-dev libtracker-sparql-1.0-dev
libtracker-miner-1.0-dev file"  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update \  
&& apt-get install \  
\--no-install-recommends \  
\--fix-missing \  
\--assume-yes \  
$DEPS \  
tracker \  
avahi-daemon \  
python \  
samba \  
supervisor \  
curl wget \  
&& wget
"http://ufpr.dl.sourceforge.net/project/netatalk/netatalk/3.1.8/netatalk-3.1.8.tar.gz"
\  
&& curl -SL
"http://ufpr.dl.sourceforge.net/project/netatalk/netatalk/3.1.8/netatalk-3.1.8.tar.gz"
| tar xvz  
  
WORKDIR netatalk-3.1.8  
  
RUN ./configure \  
\--prefix=/usr \  
\--sysconfdir=/etc \  
\--with-init-style=debian-systemd \  
\--without-libevent \  
\--without-tdb \  
\--with-cracklib \  
\--enable-krbV-uam \  
\--with-pam-confdir=/etc/pam.d \  
\--with-dbus-sysconf-dir=/etc/dbus-1/system.d \  
\--with-tracker-pkgconfig-version=1.0 \  
&& make \  
&& make install \  
&& apt-get --quiet --yes purge --auto-remove \  
$DEPS \  
tracker-gui \  
libgl1-mesa-dri \  
&& DEBIAN_FRONTEND=noninteractive apt-get install --yes \  
libevent-2.0 \  
libavahi-client3 \  
libevent-core-2.0 \  
libwrap0 \  
libtdb1 \  
libmysqlclient18 \  
libcrack2 \  
libdbus-glib-1-2 \  
&& apt-get --quiet --yes autoclean \  
&& apt-get --quiet --yes autoremove \  
&& apt-get --quiet --yes clean \  
&& rm -rf /netatalk* \  
&& rm -rf /usr/share/man \  
&& rm -rf /usr/share/doc \  
&& rm -rf /usr/share/icons \  
&& rm -rf /usr/share/poppler \  
&& rm -rf /usr/share/mime \  
&& rm -rf /usr/share/GeoIP \  
&& rm -rf /var/lib/apt/lists* \  
&& mkdir /media/share  
  
# Copy runtime files  
WORKDIR /  
COPY dropbox-dist /dropbox-dist/  
COPY dropbox.py /usr/sbin/  
COPY install.conf /etc/supervisor/conf.d/install.conf  
COPY run.conf /  
RUN chmod +x /usr/sbin/dropbox.py  
COPY run_once.sh /run_once.sh  
RUN chmod +x run_once.sh  
COPY dropbox-monitor.sh /dropbox-monitor.sh  
RUN chmod +x dropbox-monitor.sh  
COPY afp.conf /etc/afp.conf  
COPY smb.conf /etc/samba/smb.conf  
  
# expose for lansync: to enable must run with --net='host'  
EXPOSE 17500 17500/udp  
# expose supervisor http server  
EXPOSE 8000  
# expose netatalk ports  
EXPOSE 548 636 5353/udp  
# expose windows shares  
EXPOSE 137/udp 138/udp 139 445  
# enabling both ephemeral and static mapping of the volume  
VOLUME $HOME  
  
# set a name for the shared volume  
ENV SHARE_NAME Dropbox  
  
# run  
CMD ["sh","-c","/usr/bin/supervisord"]  

