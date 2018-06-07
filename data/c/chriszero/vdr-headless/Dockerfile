FROM chriszero/ubuntu-s6-base  
MAINTAINER chriszero <zerov83@gmail.com>  
  
WORKDIR /tmp  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
272A2CE18103B360 F529E113D0A5897C \  
&& echo deb http://ppa.launchpad.net/yavdr/main/ubuntu trusty main >
/etc/apt/sources.list.d/yavdr.list \  
&& echo deb http://ppa.launchpad.net/yavdr/stable-vdr/ubuntu trusty main >>
/etc/apt/sources.list.d/yavdr.list \  
&& echo deb http://ppa.launchpad.net/yavdr/stable-yavdr/ubuntu trusty main >>
/etc/apt/sources.list.d/yavdr.list \  
&& echo deb http://ppa.launchpad.net/gandalf-der-grosse/main/ubuntu trusty
main > /etc/apt/sources.list.d/gandalf.list \  
&& echo deb http://ppa.launchpad.net/gandalf-der-grosse/stable-vdr/ubuntu
trusty main >> /etc/apt/sources.list.d/gandalf.list  
  
RUN apt-get update -qq && \  
apt-get install -qy \  
wget \  
vdr \  
rsyslog \  
vdr-plugin-epgsearch \  
vdr-plugin-femon \  
vdr-plugin-satip \  
vdr-plugin-live \  
vdr-plugin-restfulapi \  
vdr-plugin-dvbapi \  
vdr-plugin-vnsiserver \  
vdr-plugin-vdrmanager \  
vdr-plugin-remotetimers \  
vdr-plugin-svdrpservice \  
vdr-plugin-streamdev-server \  
vdr-plugin-svdrposd \  
libmariadbclient18 uuid \  
libxml2 \  
nano && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo deb-src http://ppa.launchpad.net/yavdr/main/ubuntu trusty main >>
/etc/apt/sources.list.d/yavdr.list \  
&& echo deb-src http://ppa.launchpad.net/yavdr/stable-vdr/ubuntu trusty main
>> /etc/apt/sources.list.d/yavdr.list  
  
RUN apt-get update -qq && \  
apt-get install -qy build-essential libmariadbclient-dev uuid-dev libjansson4
libjansson-dev python libpython2.7 libpython-dev python-dev libarchive13
libarchive-dev libxml2-dev && \  
apt-get build-dep -qy \  
vdr-plugin-satip && \  
wget https://github.com/rofafor/vdr-plugin-satip/archive/vdr-2.2.x.tar.gz &&\  
tar xzf vdr-2.2.x.tar.gz && \  
cd vdr-plugin-satip* && \  
make && make install && \  
cd .. && wget https://projects.vdr-developer.org/git/vdr-plugin-
epg2vdr.git/snapshot/vdr-plugin-epg2vdr-1.1.58.tar.gz && \  
tar xzf vdr-plugin-epg2vdr-* && \  
cd vdr-plugin-epg2vdr* && \  
make && make install && \  
apt-get purge -qy binutils build-essential bzip2 cpp cpp-4.8 dpkg-dev fakeroot
g++ g++-4.8 gcc \  
gcc-4.8 libalgorithm-diff-perl libalgorithm-diff-xs-perl \  
libalgorithm-merge-perl libasan0 libatomic1 libc-dev-bin libc6-dev \  
libcloog-isl4 libdpkg-perl libfakeroot libfile-fcntllock-perl libgcc-4.8-dev \  
libgmp10 libisl10 libitm1 libmpc3 libmpfr4 libquadmath0 libstdc++-4.8-dev \  
libtimedate-perl libtsan0 linux-libc-dev make manpages manpages-dev patch \  
xz-utils libmariadbclient-dev uuid-dev libjansson-dev libpython-dev python-dev
libarchive-dev libxml2-dev && \  
apt-get autoremove -qy $(apt-cache showsrc vdr-plugin-satip | sed -e '/Build-
Depends/!d;s/Build-Depends: \|,\|([^)]*),*\|\\[[^]]*\\]//g') && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY vdr.sh /etc/services.d/vdr/run  
COPY vdr-finish.sh /etc/services.d/vdr/finish  
COPY rsyslog.sh /etc/services.d/rsyslog/run  
  
# Configure the vdr user account and it's folders  
RUN groupmod -o -g 666 vdr \  
&& usermod -o -u 666 vdr \  
&& install -o vdr -g vdr -d /recordings /vdr/config /vdr/cache  
  
# add configs  
COPY var/lib/vdr/* /var/lib/vdr/  
COPY var/lib/vdr/plugins/streamdev-server/* /var/lib/vdr/plugins/streamdev-
server/  
COPY etc/vdr/conf.d/* /etc/vdr/conf.d/  
COPY etc/rsyslog.conf /etc/  
  
EXPOSE 2004 3000 6419 8002 8008 4010-4020/udp 34890  
VOLUME /recordings /etc/vdr /vdr/config /vdr/cache  
  
ENTRYPOINT ["/init"]  
  

