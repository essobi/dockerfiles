FROM ubuntu:xenial  
  
ENV GOSU_VERSION 1.7  
  
ENV ARCH1C=amd64 \  
DIR1C=/opt/1C/v8.3/x86_64 \  
RAGENT=/opt/1C/v8.3/x86_64/ragent  
  
RUN if [ $ARCH1C -eq "i386" ]; then dpkg --add-architecture i386; fi \  
&& set -x \  
&& apt-get update \  
&& deps1c=" \  
imagemagick:$ARCH1C \  
imagemagick-6.q16:$ARCH1C \  
unixodbc:$ARCH1C \  
t1utils:$ARCH1C \  
libgsf-bin:$ARCH1C \  
" \  
&& buildDeps=' \  
ca-certificates \  
wget \  
xfonts-utils \  
cabextract \  
locales \  
' \  
&& apt-get install -y --no-install-recommends \  
$buildDeps \  
$deps1c \  
  
# ms fonts extract  
&& cd /tmp \  
&& wget http://ftp.debian.org/debian/pool/contrib/m/msttcorefonts/ttf-
mscorefonts-installer_3.6_all.deb \  
&& dpkg -i ttf-mscorefonts-installer_3.6_all.deb \  
&& rm ttf-mscorefonts-installer_3.6_all.deb \  
  
# install gosu  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture).asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
  
&& locale-gen en_US ru_RU ru_RU.UTF-8 \  
# set default locale  
&& echo "\  
LANGUAGE=en_US.UTF-8\n\  
LC_ALL=en_US.UTF-8\n\  
LC_CTYPE=UTF-8\n\  
LANG=en_US.UTF-8\n"\  
> /etc/default/locale \  
# set keyboard setting  
&& echo "\  
XKBMODEL=pc105\n\  
XKBLAYOUT=us,ru\n\  
XKBVARIANT=,\n\  
XKBOPTIONS=grp:alt_shift_toggle,grp_led:scroll"\  
>> /etc/default/keyboard \  
# set environment  
&& echo TERM=xterm >> /etc/environment \  
  
# clear  
&& apt-get purge -y --auto-remove $buildDeps \  
&& rm -rf /var/lib/apt/lists/* /tmp/*  
  
ENV LANG ru_RU.utf8  
  
ADD ./docker-entrypoint-init.d /docker-entrypoint-init.d  
ADD docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 1540-1541 1560-1591  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["ragent"]  

