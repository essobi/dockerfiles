FROM ubuntu:16.04  
MAINTAINER Michal Fojtak <mfojtak@seznam.cz>  
RUN echo root:$apr1$JzWS076e$17BXHnBFSbcP5JJbtMTBE0 | chpasswd -e && \  
echo "Acquire::GzipIndexes \"false\"; Acquire::CompressionTypes::Order::
\"gz\";" >/etc/apt/apt.conf.d/docker-gzip-indexes && \  
apt-get update && apt-get install -y software-properties-common language-pack-
en-base && LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/apache2 && apt-
get update && \  
apt install -y apache2 libapache2-mod-auth-openidc psmisc v4l-utils nano wget
git cmake autoconf automake build-essential libass-dev libfreetype6-dev \  
libsdl2-dev libtheora-dev libtool libva-dev libvdpau-dev libvorbis-dev
libxcb1-dev libxcb-shm0-dev \  
libxcb-xfixes0-dev pkg-config texinfo zlib1g-dev yasm mercurial libx264-dev
libvpx-dev && \  
a2enmod expires && a2enmod auth_openidc && a2enmod ssl && a2enmod http2 && \  
apt install -y perl libnet-ssleay-perl openssl libauthen-pam-perl libpam-
runtime libio-pty-perl apt-show-versions python && \  
wget http://prdownloads.sourceforge.net/webadmin/webmin_1.831_all.deb && dpkg
--install webmin_1.831_all.deb  
  
RUN hg clone https://bitbucket.org/multicoreware/x265 && cd x265/build/linux
&& cmake ../../source && make && make install && ldconfig && cd /  
RUN git clone https://github.com/qflow/FFmpeg.git ffmpeg && cd ffmpeg &&
./configure --enable-gpl --enable-libvpx --enable-libx264 --enable-libx265
--enable-nonfree && \  
make && make install  
ADD apache2.conf /etc/apache2/apache2.conf  
ADD .htpasswd /etc/apache2  
ADD 000-default.conf /etc/apache2/sites-enabled  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
ADD video.html /var/www/html  
VOLUME /data  
EXPOSE 80 443 10000  
ENTRYPOINT ["/start.sh"]  

