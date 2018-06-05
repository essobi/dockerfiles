from golang:alpine  
  
run apk update && apk add alpine-sdk git iw  
  
run go get github.com/jonnrb/docker_utils/get_bridge_name  
  
run wget https://w1.fi/releases/hostapd-2.6.tar.gz && \  
tar xzf hostapd-2.6.tar.gz  
  
# add security patches  
run cd hostapd-2.6 && \  
wget https://w1.fi/security/2017-1/rebased-v2.6-0001-hostapd-Avoid-key-
reinstallation-in-FT-handshake.patch && \  
patch -s -p1 < rebased-v2.6-0001-hostapd-Avoid-key-reinstallation-in-FT-
handshake.patch && \  
wget https://w1.fi/security/2017-1/rebased-v2.6-0002-Prevent-reinstallation-
of-an-already-in-use-group-ke.patch && \  
patch -s -p1 < rebased-v2.6-0002-Prevent-reinstallation-of-an-already-in-use-
group-ke.patch && \  
wget https://w1.fi/security/2017-1/rebased-v2.6-0003-Extend-protection-of-GTK-
IGTK-reinstallation-of-WNM-.patch && \  
patch -s -p1 < rebased-v2.6-0003-Extend-protection-of-GTK-IGTK-reinstallation-
of-WNM-.patch && \  
wget https://w1.fi/security/2017-1/rebased-v2.6-0004-Prevent-installation-of-
an-all-zero-TK.patch && \  
patch -s -p1 < rebased-v2.6-0004-Prevent-installation-of-an-all-zero-TK.patch
&& \  
wget https://w1.fi/security/2017-1/rebased-v2.6-0005-Fix-PTK-rekeying-to-
generate-a-new-ANonce.patch && \  
patch -s -p1 < rebased-v2.6-0005-Fix-PTK-rekeying-to-generate-a-new-
ANonce.patch && \  
wget https://w1.fi/security/2017-1/rebased-v2.6-0006-TDLS-Reject-TPK-TK-
reconfiguration.patch && \  
patch -s -p1 < rebased-v2.6-0006-TDLS-Reject-TPK-TK-reconfiguration.patch && \  
wget https://w1.fi/security/2017-1/rebased-v2.6-0008-FT-Do-not-allow-multiple-
Reassociation-Response-fram.patch && \  
patch -s -p1 < rebased-v2.6-0008-FT-Do-not-allow-multiple-Reassociation-
Response-fram.patch  
  
# configure, build, install  
run cd hostapd-2.6 && \  
cd hostapd && \  
cp defconfig .config && \  
sed -i '/CONFIG_ACS=y/s/^#//' .config && \  
sed -i '/CONFIG_TLSV11=y/s/^#//' .config && \  
sed -i '/CONFIG_TLSV12=y/s/^#//' .config && \  
sed -i '/CONFIG_IEEE80211AC=y/s/^#//' .config && \  
sed -i '/CONFIG_IEEE80211N=y/s/^#//' .config && \  
apk add linux-headers libnl libnl-dev openssl openssl-dev && \  
make && \  
make install  
  
# clean up image  
run rm -rf hostapd-2.6 hostapd-2.6.tar.gz && \  
apk del linux-headers libnl-dev openssl-dev alpine-sdk git && \  
rm -rf /var/cache/apk  
  
add init.sh /  
cmd ["/init.sh"]  

