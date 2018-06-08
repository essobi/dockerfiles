FROM resin/rpi-raspbian:stretch  
MAINTAINER Patrick Eichmann <phreakazoid@phreakazoid.com>  
  
ARG TZ="Europe/Berlin"  
ARG DEBIAN_FRONTEND=noninteractive  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
ARG SAMBA-Version="4.7.0rc5"  
LABEL build_version="Build-date:- ${BUILD_DATE}"  
  
RUN [ "cross-build-start" ]  
  
# SAMBA  
# NEEDED PACKAGES  
RUN apt-get -y install wget gcc make build-essential libssl1.0-dev libkrb5-dev
ntp libacl1-dev python-dev cups\  
libldap2-dev pkg-config gdb libgnutls28-dev libblkid-dev\  
libreadline-dev libattr1-dev python-dnspython libpopt-dev\  
libbsd-dev attr docbook-xsl libcups2-dev krb5-user git  
  
RUN git clone https://github.com/samba-team/samba.git /tmp/samba4/ && cd
/tmp/samba4 && git checkout tags/samba-4.7.0rc5  
RUN cd /tmp/samba4 && ./configure --enable-debug  
RUN make -C /tmp/samba4  
RUN make install -C /tmp/samba4  
  
### CLEANUP ###  
RUN apt-get purge -y gcc* make*  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN [ "cross-build-end" ]  
  
VOLUME ["/usr/local/samba/etc", "/usr/local/samba/private",
"/usr/local/samba/var"]  
# USE HOST NETWORKING  
#EXPOSE 88 135 137 138 139 389 445 464 636 3268 3269  
ENTRYPOINT ["/entrypoint.sh"]  
# START SAMBA  
CMD ["/usr/local/samba/sbin/smbd, "-D", "\--option=server role
check:inhibit=yes", "\--foreground"]  
# START WINBIND  
CMD ["/usr/local/samba/sbin/winbindd", "-D", "\--option=server role
check:inhibit=yes", "\--foreground"]  

