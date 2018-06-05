FROM buildpack-deps:bionic-curl  
  
ARG SAMBA_VERSION=4.8.0rc3  
  
ARG S6_VERSION=1.21.2.2  
  
RUN set -ex; \  
sed -i -r 's/^# *(deb.*)$/\1/' /etc/apt/sources.list ;\  
BUILD_DEPS='bison \  
debhelper \  
dh-python \  
docbook-xml \  
docbook-xsl \  
flex \  
libacl1-dev \  
libarchive-dev \  
libattr1-dev \  
libavahi-client-dev \  
libavahi-common-dev \  
libblkid-dev \  
libbsd-dev \  
libcap-dev \  
libcephfs-dev \  
libcmocka-dev \  
libcups2-dev \  
libdbus-1-dev \  
libgnutls28-dev \  
libgpgme11-dev \  
libjansson-dev \  
libldap2-dev \  
libldb-dev \  
libncurses5-dev \  
libpam0g-dev \  
libparse-yapp-perl \  
libpcap-dev \  
libpopt-dev \  
libreadline-dev \  
libsystemd-dev \  
libtalloc-dev \  
libtdb-dev \  
libtevent-dev \  
perl \  
pkg-config \  
po-debconf \  
python-all-dev \  
python-dnspython \  
python-ldb \  
python-ldb-dev \  
python-talloc-dev \  
python-tdb \  
python-testtools \  
python3 \  
xfslibs-dev \  
xsltproc \  
zlib1g-dev' ;\  
apt-get update; \  
apt-get -y dist-upgrade --autoremove ;\  
apt-get -y --no-install-recommends install $BUILD_DEPS ;\  
adduser --disabled-password --gecos 'TimeMachine' timemachine ;\  
mkdir -p /tmp ;\  
cd /tmp ;\  
wget https://github.com/just-
containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz
;\  
tar -xzf s6-overlay-amd64.tar.gz -C / ;\  
rm s6-overlay-amd64.tar.gz ;\  
cd /tmp ;\  
su timemachine -m -c "wget
https://download.samba.org/pub/samba/rc/samba-${SAMBA_VERSION}.tar.gz" ;\  
su timemachine -m -c "tar -xzvf samba-${SAMBA_VERSION}.tar.gz" ;\  
cd /tmp/samba-${SAMBA_VERSION} ;\  
su timemachine -m -c "./configure --prefix=/usr \  
\--enable-fhs \  
\--sysconfdir=/etc \  
\--localstatedir=/var \  
\--with-privatedir=/var/lib/samba/private \  
\--with-smbpasswd-file=/etc/samba/smbpasswd \  
\--with-piddir=/var/run/samba \  
\--with-pammodulesdir=/lib/$(DEB_HOST_MULTIARCH)/security \  
\--with-pam \  
\--with-syslog \  
\--with-utmp \  
\--with-winbind \  
\--with-shared-
modules=idmap_rid,idmap_ad,idmap_adex,idmap_hash,idmap_ldap,idmap_tdb2,vfs_dfs_samba4,auth_samba4
\  
\--with-automount \  
\--with-ldap \  
\--with-ads \  
\--with-dnsupdate \  
\--with-gpgme \  
\--datadir=/usr/share \  
\--with-lockdir=/var/run/samba \  
\--with-statedir=/var/lib/samba \  
\--with-cachedir=/var/cache/samba \  
\--enable-avahi \  
\--disable-rpath \  
\--disable-rpath-install \  
\--with-cluster-support \  
\--with-socketpath=/var/run/ctdb/ctdbd.socket \  
\--with-logdir=/var/log/ctdb \  
\--libexecdir=/usr/lib/$(DEB_HOST_MULTIARCH) \  
\--builtin-libraries=ccan,samba-cluster-support \  
\--minimum-library-version=\"$(shell ./debian/autodeps.py --minimum-library-
version)\" \  
\--libdir=/usr/lib/$(DEB_HOST_MULTIARCH) \  
\--with-modulesdir=/usr/lib/$(DEB_HOST_MULTIARCH)/samba" ;\  
su timemachine -m -c "make -j$(nproc)" ;\  
make install ;\  
cd /tmp ;\  
rm -rf --one-file-system /tmp/samba* ;\  
apt-get autoremove --purge -y $BUILD_DEPS ;\  
rm -rf /var/lib/apt/lists/*  
  
COPY etc /etc  
COPY smb.conf /  
  
EXPOSE 137/UDP 138/UDP 139/TCP 445/TCP  
VOLUME ["/time-capsule", "/etc/samba"]  
  
ENV SMBPASSWD=tmpass  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="SMB TimeMachine" \  
org.label-schema.description="Builds Samba for use as a time capsule for time
machine. Supports the various vfs_fruit attributes to allow compatibility with
newer versions of OS X." \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/mumblepins-docker/smb-
timemachine" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="1.0"  
  
ENTRYPOINT ["/init"]  
  

