FROM akohlbecker/base:18.04  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
curl ca-certificates \  
acl attr autoconf bind9utils bison build-essential \  
debhelper dnsutils docbook-xml docbook-xsl flex gdb libjansson-dev krb5-user \  
libacl1-dev libaio-dev libarchive-dev libattr1-dev libblkid-dev libbsd-dev \  
libcap-dev libcups2-dev libgnutls28-dev libgpgme-dev libjson-perl \  
libldap2-dev libncurses5-dev libpam0g-dev libparse-yapp-perl \  
libpopt-dev libreadline-dev libsystemd-dev nettle-dev perl perl-modules pkg-
config \  
python-all-dev python-crypto python-dbg python-dev python-dnspython \  
python3-dnspython python-gpg python3-gpg python-markdown python3-markdown \  
python3-dev xsltproc zlib1g-dev \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -x \  
&& curl -OL https://download.samba.org/pub/samba/stable/samba-4.8.1.tar.gz \  
&& echo "8ef7367507f16b7a5e2f6aed5bcdbd1143feca79aa2a07c9b21292b17d7f789d
samba-4.8.1.tar.gz" | sha256sum -c - \  
&& tar -xzf samba-4.8.1.tar.gz \  
&& rm samba-4.8.1.tar.gz \  
&& cd samba-4.8.1 \  
&& ./configure --jobs=`nproc --all` --prefix=/usr --sysconfdir=/etc
--localstatedir=/var \--enable-fhs \  
&& make --jobs=`nproc --all` \  
&& make install \  
&& rm -rf samba-4.8.1  
  
RUN set -x && \  
groupadd --gid 2000 media && \  
groupadd --gid 1000 adrien && \  
groupadd --gid 2006 sonos && \  
useradd --uid 1000 \--gid 1000 \--no-create-home --groups media adrien && \  
useradd --uid 2006 \--gid 2006 \--no-create-home --groups media sonos  
USER root  
  
EXPOSE 137/udp 138/udp 139 445  
  
ADD app /app  
WORKDIR /app  
  
CMD ["/app/boot", "smbd", "--interactive", "--debuglevel=2"]  

