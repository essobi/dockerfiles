# docker image for ostinato  
  
FROM debian:stretch-slim  
  
COPY ostinato*.deb python-ostinato*.tar.gz libpcap*.deb /tmp/  
  
RUN set -ex \  
#  
# install ostinato  
#  
&& export DEBIAN_FRONTEND=noninteractive \  
&& echo 'wireshark-common wireshark-common/install-setuid boolean false' |
debconf-set-selections \  
&& apt-get update \  
&& apt-get -y --no-install-recommends install \  
dumb-init /tmp/ostinato*.deb /tmp/libpcap*.deb wireshark tshark dillo
lxterminal jwm menu leafpad \  
net-tools iproute2 ifupdown isc-dhcp-client inetutils-ping \  
telnet traceroute procps nano vim-tiny \  
&& apt-get -y --no-install-recommends install \  
python python-pip python-setuptools python-wheel python-protobuf \  
&& pip install --no-cache-dir /tmp/python-ostinato*.tar.gz \  
&& rm -rf /var/lib/apt/lists/* \  
#  
# customize jwm menu  
#  
&& /bin/echo -e '\  
?package(ostinato):\\\n\  
needs="x11"\\\n\  
section="Applications"\\\n\  
title="Ostinato"\\\n\  
command="ostinato > /var/log/ostinato.log 2>&1"' \  
> /etc/menu/ostinato \  
&& /bin/echo -e '\  
?package(wireshark):\\\n\  
needs="x11"\\\n\  
section="Applications"\\\n\  
title="Wireshark"\\\n\  
command="wireshark"' \  
> /etc/menu/wireshark \  
&& echo "postrun="\""sed -i '/^ </ d' debian-menu"\" >> /etc/menu-methods/jwm
\  
&& sed -i 's/\(Desktops width\)="[0-9]*"/\1="2"/' /etc/jwm/system.jwmrc \  
&& sed -i 's/xterm/x-terminal-emulator/g' /etc/jwm/system.jwmrc \  
&& update-menus \  
#  
# configure ostinato drone  
#  
&& mkdir -p /root/.config/Ostinato \  
&& /bin/echo -e '\  
[General]\n\  
RateAccuracy=Low\n\  
[PortList]\n\  
Include=eth*' \  
> /root/.config/Ostinato/drone.ini \  
#  
# configure wireshark  
#  
&& sed -i 's/^disable_lua *=.*/disable_lua = true/' /etc/wireshark/init.lua \  
#  
# set lxterminal defaults  
#  
&& mkdir -p /root/.config/lxterminal \  
&& /bin/echo -e '\  
[general]\n\  
scrollback=1000\n\  
fgcolor=#ffffff' \  
> /root/.config/lxterminal/lxterminal.conf \  
#  
# startup script  
#  
&& /bin/echo -e '\  
\x23!/bin/sh\n\  
[ $$ -eq 1 ] && exec dumb-init -- "$0" "$@"\n\  
\n\  
\x23 on unconfigured interfaces disable IPv6, set MTU to 9000\n\  
sed -n '\''s/^ *\\(eth[0-9]*\\):.*/\\1/p'\'' /proc/net/dev | sort >
/tmp/netdev\n\  
sed -n '\''s/^iface *\\(eth[0-9]*\\).*/\\1/p'\'' /etc/network/interfaces |
sort -u > /tmp/confdev\n\  
for DEVICE in `comm -13 /tmp/confdev /tmp/netdev`; do\n\  
ip link set dev $DEVICE down\n\  
sysctl -q -w net.ipv6.conf.$DEVICE.disable_ipv6=1\n\  
ip link set dev $DEVICE mtu 9000\n\  
ip link set dev $DEVICE up\n\  
done\n\  
rm /tmp/confdev /tmp/netdev\n\  
sleep 0.5\n\  
\n\  
\x23 disable ostinato update, makes no sense in this environment\n\  
fgrep -q -w update.ostinato.org /etc/hosts || \\\n\  
/bin/echo -e "\\n# disable ostinato
update\\n127.0.0.127\\tupdate.ostinato.org" >> /etc/hosts\n\  
\n\  
\x23 wireshark wants a /etc/machine-id\n\  
dd if=/dev/urandom bs=16 count=1 2>/dev/null | od -An -x | tr -d " " >
/etc/machine-id\n\  
\n\  
\x23 workaround: sometimes the first start of an X application fails\n\  
lxterminal -e true 2> /dev/null\n\  
\n\  
cd\n\  
export SHELL=/bin/bash\n\  
ostinato > /var/log/ostinato.log 2>&1 &\n\  
jwm' \  
> /etc/init.sh && chmod +x /etc/init.sh  
  
VOLUME [ "/root" ]  
CMD [ "/etc/init.sh" ]  

