FROM alpine:latest  
  
RUN apk add --no-cache \  
wget \  
curl \  
unzip  
  
ADD aspcud /usr/bin/aspcud  
  
ENV LIQUIDSOAP_VERSION=1.2.1  
  
RUN cp /etc/apk/repositories /etc/apk/repositories.orig \  
&& echo http://www.cl.cam.ac.uk/~avsm2/alpine-ocaml/ >> /etc/apk/repositories
\  
&& echo http://dl-4.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
&& cd /etc/apk/keys && curl -OL http://www.cl.cam.ac.uk/~avsm2/alpine-
ocaml/x86_64/anil@recoil.org-5687cc79.rsa.pub \  
&& apk add --no-cache --virtual .build-deps \  
alpine-sdk \  
alsa-lib-dev \  
autoconf \  
automake \  
bash \  
bison \  
bzip2 \  
bzip2-dev \  
ca-certificates \  
cairo-dev \  
camlp4 \  
cmake \  
curl-dev \  
# dssi-dev \  
faad2-dev \  
fdk-aac-dev \  
# ffmpeg-dev \  
fftw-dev \  
file \  
flac-dev \  
flex \  
freetype-dev \  
g++ \  
gawk \  
gcc \  
gst-plugins-bad1-dev \  
gst-plugins-base1-dev \  
gstreamer1-dev \  
jack-dev \  
# ladspa-dev \  
lame-dev \  
libao-dev \  
# liblo-dev \  
libmad-dev \  
libogg-dev \  
liboil-dev \  
libsamplerate-dev \  
libtheora-dev \  
libtool \  
libvorbis-dev \  
m4 \  
ncurses-dev \  
ocaml \  
opam \  
opus-dev \  
orc-compiler \  
orc-dev \  
patch \  
pcre-dev \  
portaudio-dev \  
# pulseaudio-dev \  
rsync \  
soundtouch-dev \  
speex-dev \  
speexdsp-dev \  
taglib-dev \  
&& adduser -S opam \  
&& chown -R opam /usr/local \  
&& export OPAMCOLOR=newer \  
&& export PKG_CONFIG_PATH="/usr/lib/pkgconfig:/usr/local/lib/pkgconfig" \  
&& echo 'opam ALL=(ALL:ALL) NOPASSWD:ALL' > /etc/sudoers.d/opam \  
&& chmod 440 /etc/sudoers.d/opam \  
&& chown root:root /etc/sudoers.d/opam \  
&& sed -i.bak 's/^Defaults.*requiretty//g' /etc/sudoers \  
&& mkdir -p /usr/local/src \  
&& cd /usr/local/src \  
&& wget
"http://tipok.org.ua/downloads/media/aacplus/libaacplus/libaacplus-2.0.2.tar.gz"
\  
&& tar -zxvf libaacplus-2.0.2.tar.gz \  
&& cd libaacplus-2.0.2 \  
&& ./autogen.sh --enable-shared --enable-static \  
&& make \  
&& make install \  
&& cd /usr/local/src \  
&& curl -sS
http://netix.dl.sourceforge.net/project/gmerlin/gavl/1.4.0/gavl-1.4.0.tar.gz |
tar -xz \  
&& curl -sS https://files.dyne.org/frei0r/frei0r-plugins-1.5.0.tar.gz | tar
-xz \  
&& curl -sS http://netix.dl.sourceforge.net/project/opencore-amr/vo-aacenc/vo-
aacenc-0.1.3.tar.gz | tar -xz \  
&& cd /usr/local/src/gavl-1.4.0 \  
&& CFLAGS="-D_GNU_SOURCE" ./configure --without-doxygen \  
&& CFLAGS="-D_GNU_SOURCE" make all install \  
&& cd /usr/local/src/vo-aacenc-0.1.3 \  
&& ./configure \  
&& make all install \  
&& cd /usr/local/src/frei0r-plugins-1.5.0 \  
&& cmake . \  
&& make all install \  
&& cd /usr/local/src \  
&& curl -sS
https://launchpadlibrarian.net/149460206/schroedinger-1.0.11.tar.gz | tar -xz
\  
&& cd /usr/local/src/schroedinger-1.0.11 \  
&& ./configure \  
&& make all install \  
&& cd /home/opam \  
&& install -o opam -m700 -d /home/opam/.ssh \  
&& git config --global user.email "docker@example.com" \  
&& git config --global user.name "Docker CI" \  
&& sudo -u opam sh -c "git clone git://github.com/ocaml/opam-repository" \  
&& sudo -u opam sh -c "opam init -a -y /home/opam/opam-repository" \  
&& sudo -u opam sh -c "opam pin add depext https://github.com/ocaml/opam-
depext.git" \  
&& sudo -u opam sh -c "opam install -y depext travis-opam" \  
&& sudo -u opam sh -c "opam install -y \  
alsa \  
ao \  
bjack \  
cry \  
cry \  
# dssi \  
faad \  
fdkaac \  
# ffmpeg \  
flac \  
inotify \  
# ladspa \  
lame \  
# lastfm \  
# lo \  
mad \  
ogg \  
opus \  
portaudio \  
# pulseaudio \  
samplerate \  
soundtouch \  
speex \  
taglib \  
theora \  
vorbis \  
xmlplaylist" \  
&& sudo -u opam sh -c "PKG_CONFIG_PATH=$PKG_CONFIG_PATH
CFLAGS=-I/usr/local/include opam install -y \  
voaacenc \  
schroedinger \  
gavl \  
frei0r \  
aacplus" \  
&& sudo -u opam sh -c "PKG_CONFIG_PATH=$PKG_CONFIG_PATH
CFLAGS=-I/usr/local/include opam install -y liquidsoap=$LIQUIDSOAP_VERSION" \  
&& rm -rf /usr/local/src \  
&& for dir in sbin bin doc etc lib man share; do \  
mv /home/opam/.opam/system/$dir/* /usr/local/$dir \  
&& rmdir /home/opam/.opam//system/$dir \  
&& ln -s /usr/local/$dir /home/opam/.opam/system/$dir \  
; done \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .rundeps $runDeps \  
&& apk del .build-deps \  
&& mv -f /etc/apk/repositories.orig /etc/apk/repositories \  
&& rm -f /etc/apk/keys/anil@recoil.org-5687cc79.rsa.pub \  
&& rm -fr /home/opam/.opam/log/* /home/opam/.opam/packages.dev/*
/home/opam/.opam/system/packages.dev/* \  
&& install -o opam -d /var/run/liquidsoap  
  
USER opam  
CMD ["liquidsoap"]  
  
  
  
  

