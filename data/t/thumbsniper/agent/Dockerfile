FROM opensuse:42.3  
MAINTAINER Thomas Schulte <thomas@cupracer.de>  
  
CMD ["/start.sh"]  
  
RUN zypper --non-interactive in curl  
  
RUN rpm --import \  
http://download.opensuse.org/repositories/home:/TERROR-
FX:/thumbsniper:/utilities/openSUSE_Leap_42.3/repodata/repomd.xml.key \  
http://download.opensuse.org/repositories/Publishing/openSUSE_Leap_42.3/repodata/repomd.xml.key
\  
http://download.opensuse.org/repositories/devel:/languages:/php/openSUSE_Leap_42.3/repodata/repomd.xml.key
\  
http://download.opensuse.org/repositories/server:/php:/applications/openSUSE_Leap_42.3/repodata/repomd.xml.key
\  
http://download.opensuse.org/repositories/server:/php:/extensions/openSUSE_Leap_42.3/repodata/repomd.xml.key  
  
RUN /usr/bin/zypper ar --refresh
http://download.opensuse.org/repositories/home:/TERROR-
FX:/thumbsniper:/utilities/openSUSE_Leap_42.3/home:TERROR-
FX:thumbsniper:utilities.repo  
RUN /usr/bin/zypper ar --refresh
http://download.opensuse.org/repositories/Publishing/openSUSE_Leap_42.3/Publishing.repo  
RUN /usr/bin/zypper ar --refresh
http://download.opensuse.org/repositories/devel:/languages:/php/openSUSE_Leap_42.3/devel:languages:php.repo  
RUN /usr/bin/zypper ar --refresh
http://download.opensuse.org/repositories/server:/php:/applications/openSUSE_Leap_42.3/server:php:applications.repo  
RUN /usr/bin/zypper ar --refresh
http://download.opensuse.org/repositories/server:/php:/extensions/openSUSE_Leap_42.3/server:php:extensions.repo  
  
RUN zypper --non-interactive ref && zypper --non-interactive in \  
bc \  
ca-certificates-mozilla \  
cutycapt \  
git \  
glibc-extra \  
glibc-locale \  
ImageMagick \  
libQtWebKit4 \  
php-composer \  
php5 \  
php5-bz2 \  
php5-ctype \  
php5-curl \  
php5-exif \  
php5-gd \  
php5-gettext \  
php5-imagick \  
php5-intl \  
php5-json \  
php5-mbstring \  
php5-openssl \  
php5-zip \  
php5-zlib \  
wkhtmltopdf \  
xorg-x11-server \  
dejavu-fonts \  
efont-unicode-bitmap-fonts \  
ghostscript-fonts-other \  
ghostscript-fonts-std \  
google-droid-fonts \  
intlfonts \  
intlfonts-euro-bitmap-fonts \  
liberation-fonts \  
patterns-openSUSE-fonts_opt \  
xorg-x11-fonts \  
tar  
  
RUN /usr/sbin/groupadd -g 999 tagent  
RUN /usr/sbin/useradd -u 999 -g 999 -c tagent -m -s /bin/bash tagent  
  
ADD
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
/tmp  
#COPY phantomjs-2.1.1-linux-x86_64.tar.bz2 /tmp  
RUN mkdir /opt/phantomjs && tar xf /tmp/phantomjs-2.1.1-linux-x86_64.tar.bz2
--strip 1 -C /opt/phantomjs  
  
COPY etc/php5 /etc/php5  
  
#RUN git clone -b master https://github.com/thumbsniper/agent.git
/opt/thumbsniper  
RUN git clone -b v0.9.7 https://github.com/thumbsniper/agent.git
/opt/thumbsniper  
  
RUN composer --working-dir=/opt/thumbsniper update  
  
COPY config/agent-config.inc.php /opt/thumbsniper/config/agent-config.inc.php  
COPY start.sh /start.sh  
  
RUN zypper --non-interactive up  
  
USER tagent  
  

