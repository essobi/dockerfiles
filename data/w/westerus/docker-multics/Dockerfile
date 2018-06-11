#  
# Build: docker build -t multics .  
# Run: docker run -d -p 5500:5500 --name multics-run multics  
#  
FROM ubuntu:trusty  
MAINTAINER Westerus <westerus@gmail.com>  
LABEL Description="This image is used to start multics service" \  
Version="1.0-r82"  
  
ARG PKG_FLAGS_COMMON="-qq -y"  
ARG PKG_FLAGS_PERSISTANT="${PKG_FLAGS_COMMON} --no-install-recommends"  
ARG PKG_FLAGS_DEV="${PKG_FLAGS_COMMON} --no-install-recommends"  
ARG PKGUPDATE="apt-get ${PKG_FLAGS_COMMON} update"  
ARG PKGUPGRADE="apt-get ${PKG_FLAGS_PERSISTANT} upgrade"  
ARG PKGAUTOREMOVE="apt-get ${PKG_FLAGS_COMMON} autoremove"  
ARG PKGCLEAN="apt-get ${PKG_FLAGS_COMMON} clean"  
ARG DELTEMP="rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*"  
ARG PKGINSTALL="apt-get ${PKG_FLAGS_PERSISTANT} install"  
ARG PKGREMOVE="apt-get ${PKG_FLAGS_COMMON} purge"  
ENV PATH="/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/bin" \  
HOME="/root" IDIOM=es_ES CN=es TZ="Europe/Madrid" \  
TERM=xterm DEBIAN_FRONTEND=noninteractive UBUNTUTAG=trusty  
  
ENV MULTICSVER=r82  
ENV MULTICSFILE multics.${MULTICSVER}.rar  
ENV MULTICSURL http://www.infosat.org/multics  
ENV MULTICSCFG /etc/multics/multics.cfg  
ENV MULTICSBIN /usr/bin/multics  
  
ADD ${MULTICSURL}/${MULTICSFILE} /tmp  
  
RUN sed -i 's/universe$/universe multiverse/g' /etc/apt/sources.list && \  
$PKGUPDATE && $PKGUPGRADE 2>/dev/null && \  
$PKGINSTALL locales && localedef -i $IDIOM -c -f UTF-8 -A
/usr/share/locale/locale.alias ${IDIOM}.UTF-8 && \  
$PKGINSTALL unrar && \  
mkdir -p \  
/usr/src/multics \  
/etc/multics.${MULTICSVER} \  
/srv/multics.${MULTICSVER} && \  
ln -s /etc/multics.${MULTICSVER} /etc/multics && \  
ln -s /srv/multics.${MULTICSVER} /srv/multics && \  
mkdir -p /etc/multics/conf && \  
unrar e /tmp/${MULTICSFILE} /usr/src/multics/ && \  
cp /usr/src/multics/multics.x64 /srv/multics/ && \  
chmod 775 /srv/multics/multics.x64 && \  
ln -s /srv/multics/multics.x64 $MULTICSBIN && \  
ln -s /etc/multics/conf/multics.cfg $MULTICSCFG && \  
rm -rf /usr/src/multics && \  
rm /tmp/* && \  
$PKGREMOVE unrar && echo $PKGREMOVE && \  
$PKGAUTOREMOVE && $PKGCLEAN && $DELTEMP  
  
ENV LANG="${IDIOM}.UTF-8"  
COPY conf/ /etc/multics/conf/  
  
EXPOSE 5500 5500/tcp 15000 15000/tcp 26900 26900/tcp \  
4042 4042/udp 27100:27106 27100:27106/tcp 27101 27101/tcp \  
27129 27129/tcp 27139 27139/tcp 26700 26700/tcp 14000 14000/tcp \  
18800 18800/tcp 19800 19800/tcp 26800 26800/tcp 23800 23800/tcp  
  
CMD ["/usr/bin/multics","-C","/etc/multics/multics.cfg"]  

