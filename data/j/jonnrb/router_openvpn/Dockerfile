from ubuntu:xenial as build  
run apt-get update \  
&& apt-get install -y build-essential wget libssl-dev liblz4-dev liblzo2-dev \  
&& wget https://swupdate.openvpn.org/community/releases/openvpn-2.4.4.tar.gz \  
&& tar xvf openvpn-2.4.4.tar.gz \  
&& cd openvpn-2.4.4 \  
&& ./configure --disable-shared --enable-static --disable-plugin-auth-pam \  
\--disable-plugin-down-root --enable-iproute2 \  
&& make LIBS="-all-static" \  
&& make install  
run apt-get install -y git pkg-config bison flex \  
&& git clone \  
'git://git.kernel.org/pub/scm/linux/kernel/git/shemminger/iproute2.git' \  
&& cd iproute2 \  
&& ./configure \  
&& make \  
&& make install  
  
from jonnrb/router_base  
copy \--from=build /usr/local/sbin/openvpn /sbin/openvpn  
copy \--from=build /etc/iproute2 /etc/iproute2  
copy \--from=build /sbin/ip /sbin/ip  
entrypoint ["/init", "-c", "openvpn /data/openvpn.conf"]  

