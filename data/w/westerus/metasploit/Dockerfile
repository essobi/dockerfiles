FROM kalilinux/kali-linux-docker  
  
MAINTAINER Westerus <westerus@gmail.com>  
  
LABEL manteiner="Westerus <westerus@gmail.com>" \  
description="ISC Kea DHCPv4 Base" \  
version="0.1.0"  
  
ARG PKG_FLAGS_COMMON="-qq -y"  
ARG PKG_FLAGS_PERSISTANT="${PKG_FLAGS_COMMON} --no-install-recommends"  
ARG PKG_FLAGS_DEV="${PKG_FLAGS_COMMON} --no-install-recommends"  
ARG PKGUPDATE="apt-get ${PKG_FLAGS_COMMON} update"  
ARG PKGUPGRADE="apt-get ${PKG_FLAGS_COMMON} dist-upgrade"  
ARG PKGCLEAN="apt-get ${PKG_FLAGS_COMMON} autoclean"  
ARG DELTEMP="rm -rf /var/tmp/* /tmp/*"  
ARG PKGINSTALL="apt-get ${PKG_FLAGS_PERSISTANT} install"  
ARG PKGREMOVE="apt-get ${PKG_FLAGS_COMMON} remove"  
ARG PKGPURGE="apt-get ${PKG_FLAGS_COMMON} purge"  
ARG LIBREMOVE="dpkg -r --force-depends"  
ARG LIBPURGE="dpkg -P --force-depends"  
ENV DEBIAN_FRONTEND="noninteractive" TERM="xterm"  
ENV MSFUSER=metasploit  
ENV MSFPASS=M3t4Spl01t_  
ENV MSFPORT=55553  
COPY /rootfs/entry-point.sh /  
  
RUN $PKGUPDATE \  
&& $PKGUPGRADE \  
&& $PKGINSTALL ca-certificates \  
metasploit-framework \  
&& $PKGCLEAN \  
&& $DELTEMP  
  
EXPOSE 55553  
ENTRYPOINT ["/entry-point.sh"]  
CMD msfrpcd -U ${MSFUSER} -P ${MSFPASS} -f  

