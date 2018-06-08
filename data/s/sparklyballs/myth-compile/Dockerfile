FROM phusion/baseimage:0.9.16  
# Set correct environment variables  
ENV DEBIAN_FRONTEND=noninteractive HOME="/root" TERM=xterm LANG=en_US.UTF-8
LANGUAGE=en_US:en LC_ALL=en_US.UTF-8  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Expose port  
EXPOSE 3389  
# Add local files  
ADD src/ /root/  
# volumes  
VOLUME /db  
  
# Set the locale  
RUN locale-gen en_US.UTF-8 && \  
# update apt  
mv /root/excludes /etc/dpkg/dpkg.cfg.d/excludes && \  
apt-add-repository ppa:ubuntu-mate-dev/ppa && \  
apt-add-repository ppa:ubuntu-mate-dev/trusty-mate && \  
echo "deb http://archive.ubuntu.com/ubuntu/ trusty multiverse" >>
/etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty multiverse" >>
/etc/apt/sources.list && \  
echo "deb http://archive.ubuntu.com/ubuntu/ trusty-updates multiverse" >>
/etc/apt/sources.list && \  
echo "deb-src http://archive.ubuntu.com/ubuntu/ trusty-updates multiverse" >>
/etc/apt/sources.list && \  
# set startup file  
mv /root/firstrun.sh /etc/my_init.d/firstrun.sh && \  
chmod +x /etc/my_init.d/firstrun.sh && \  
# install packages and dependencies  
apt-get update -qqy && \  
apt-get install --force-yes \--no-install-recommends \  
wget \  
openjdk-7-jre \  
supervisor \  
sudo \  
nano \  
net-tools \  
x11vnc \  
xvfb \  
mate-desktop-environment-core -y && \  
# install xrdp  
apt-get install \  
xrdp -y && \  
# create ubuntu user  
useradd --create-home --shell /bin/bash --user-group --groups
adm,sudo,audio,video,cdrom,dialout ubuntu && \  
echo "ubuntu:PASSWD" | chpasswd && \  
# set user ubuntu to same uid and guid as nobody:users in unraid  
usermod -u 99 ubuntu && \  
usermod -g 100 ubuntu && \  
# swap in modified xrdp.ini  
mv /etc/xrdp/xrdp.ini /etc/xrdp/xrdp.original && \  
mv /root/xrdp.ini /etc/xrdp/xrdp.ini && \  
chown root:root /etc/xrdp/xrdp.ini && \  
# install mythtv build dependencies  
apt-get install \  
ttf-liberation \  
libfontconfig1 \  
git \  
build-essential \  
yasm \  
make \  
gcc \  
g++ \  
lame \  
libmp3lame0 \  
qt4-dev-tools \  
uuid-dev \  
libfreetype6-dev \  
libmp3lame-dev \  
libxinerama-dev \  
libtag1-dev \  
libexiv2-dev \  
libdbd-mysql-perl \  
libnet-upnp-perl \  
libdbi-perl \  
python-urlgrabber \  
python-mysqldb \  
libqt4-sql-mysql \  
libtool \  
dh-autoreconf \  
libvpx-dev \  
libx264-dev \  
libxvidcore-dev \  
python-lxml \  
libxml++2.6-dev \  
libass-dev \  
cpanminus \  
libavahi-compat-libdnssd-dev \  
libssl-dev \  
libsdl1.2-dev \  
libfaac-dev \  
libfftw3-dev \  
libqtwebkit-dev \  
libjack-dev -y && \  
# install cpan packages  
cpanm HTTP::Request LWP::UserAgent IO::Socket::INET6 && \  
# fetch source from git  
cd /tmp && \  
git clone -b fixes/0.27 git://github.com/MythTV/mythtv.git && \  
cd mythtv/mythtv && \  
# configure and compile mythtv  
./configure \  
\--enable-nonfree \  
\--enable-libmp3lame \  
\--enable-libx264 \  
\--enable-libvpx \  
\--enable-libxvid \  
\--enable-sdl \  
\--enable-libass \  
\--enable-libfaac \  
\--enable-libxml2 && \  
# make and install mythtv  
make && \  
make install && \  
# clean build dependencies and tmp files etc....  
apt-get purge --remove \  
git \  
build-essential \  
yasm \  
make \  
gcc \  
g++ -y && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

