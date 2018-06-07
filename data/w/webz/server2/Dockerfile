FROM kylemanna/openvpn  
  
RUN apk del openvpn openvpn-auth-pam && \  
apk add --update ca-certificates mysql-client make g++ libgcrypt libgcrypt-dev
unzip && \  
apk add --update git wget build-base autoconf automake libtool iproute2
libressl-dev lzo-dev linux-pam-dev linux-headers && \  
cd /tmp && \  
wget https://swupdate.openvpn.org/community/releases/openvpn-2.4.1.tar.gz && \  
tar -xzvf openvpn-2.4.1.tar.gz && \  
cd /tmp/openvpn-2.4.1 && \  
wget
https://raw.githubusercontent.com/Tunnelblick/Tunnelblick/master/third_party/sources/openvpn/openvpn-2.4.1/patches/02-tunnelblick-
openvpn_xorpatch-a.diff && \  
wget
https://raw.githubusercontent.com/Tunnelblick/Tunnelblick/master/third_party/sources/openvpn/openvpn-2.4.1/patches/03-tunnelblick-
openvpn_xorpatch-b.diff && \  
wget
https://raw.githubusercontent.com/Tunnelblick/Tunnelblick/master/third_party/sources/openvpn/openvpn-2.4.1/patches/04-tunnelblick-
openvpn_xorpatch-c.diff && \  
wget
https://raw.githubusercontent.com/Tunnelblick/Tunnelblick/master/third_party/sources/openvpn/openvpn-2.4.1/patches/05-tunnelblick-
openvpn_xorpatch-d.diff && \  
wget
https://raw.githubusercontent.com/Tunnelblick/Tunnelblick/master/third_party/sources/openvpn/openvpn-2.4.1/patches/06-tunnelblick-
openvpn_xorpatch-e.diff && \  
git apply --check 02-tunnelblick-openvpn_xorpatch-a.diff && \  
git apply 02-tunnelblick-openvpn_xorpatch-a.diff && \  
git apply --check 03-tunnelblick-openvpn_xorpatch-b.diff && \  
git apply 03-tunnelblick-openvpn_xorpatch-b.diff && \  
git apply --check 04-tunnelblick-openvpn_xorpatch-c.diff && \  
git apply 04-tunnelblick-openvpn_xorpatch-c.diff && \  
git apply --check 05-tunnelblick-openvpn_xorpatch-d.diff && \  
git apply 05-tunnelblick-openvpn_xorpatch-d.diff && \  
git apply --check 06-tunnelblick-openvpn_xorpatch-e.diff && \  
git apply 06-tunnelblick-openvpn_xorpatch-e.diff && \  
autoreconf -i -v -f && \  
./configure --build=$CBUILD \--host=$CHOST \--prefix=/usr
--mandir=/usr/share/man --sysconfdir=/etc/openvpn --enable-crypto --enable-
iproute2 && \  
make && \  
make install && \  
rm -r -f /tmp/* && \  
rm -rf /tmp/* /var/tmp/* /var/cache/apk/*  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*  
  
CMD ["/bin/bash", "-c", "set -e && pre_run"]  

