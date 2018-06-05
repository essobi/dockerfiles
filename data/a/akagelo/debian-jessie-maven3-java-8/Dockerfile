# Version: 0.0.1  
FROM debian:jessie-backports  
MAINTAINER Oleg Vyukov <gelo@vyukov.ru>  
  
  
RUN echo "deb http://ftp.ru.debian.org/debian/ jessie-backports main contrib
non-free" > /etc/apt/sources.list.d/backports.list && \  
echo "deb http://ftp.ru.debian.org/debian/ jessie main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb http://ftp.ru.debian.org/debian/ jessie-updates main contrib non-
free" >> /etc/apt/sources.list &&\  
echo "deb http://security.debian.org jessie/updates main contrib non-free" >>
/etc/apt/sources.list  
  
# locales  
RUN apt-get update && apt-get install locales-all -y \  
&& rm -rf /var/lib/apt/lists/*  
  
# maven и openjdk 8  
RUN apt-get update && apt-get install -t jessie-backports -y \  
openjdk-8-jdk \  
maven \  
git \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
#media зависимости для сборок  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y
adduser \  
geoip-database \  
libc6 \  
libcurl3-gnutls \  
libogg0 \  
libspeex1 \  
libtheora0 \  
libvorbis0a \  
libxml2 \  
libxslt1.1 \  
debconf \  
ffmpeg \  
sox \  
lame \  
libsox-fmt-mp3 \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD ./init-settings.xml.sh /init-settings.xml.sh  
  
ADD vyukov.ru.CA.crt /usr/local/share/ca-certificates/vyukov.CA.crt  
RUN update-ca-certificates

