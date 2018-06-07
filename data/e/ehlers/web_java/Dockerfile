# Web browser plus Java  
  
FROM ehlers/webterm  
  
RUN set -ex \  
#  
# install Java and Java Web Start  
#  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& mkdir -p /usr/share/man/man1 \  
&& apt-get -y --no-install-recommends install \  
icedtea-netx fonts-dejavu-extra yad \  
&& rm -rf /var/lib/apt/lists/* \  
#  
# customize jwm menu  
#  
&& /bin/echo -e '\  
?package(icedtea-netx):\\\n\  
needs="x11"\\\n\  
section="Applications"\\\n\  
title="ASDM Launcher"\\\n\  
command="start-asdm"' \  
> /etc/menu/asdm \  
&& update-menus \  
#  
# ASDM Launcher  
#  
&& /bin/echo -e '\  
\x23!/bin/sh\n\  
\n\  
asa_ip=`yad --entry --title="ASDM Launcher" \\\n\  
\--text="\\n Connects to ASAv by ASDM \\n" \\\n\  
\--entry-text="IP"`\n\  
[ $? -ne 0 ] && exit 1\n\  
[ -z "$asa_ip" -o "$asa_ip" = "IP" ] && exit 1\n\  
\n\  
javaws https://$asa_ip/admin/public/asdm.jnlp < /dev/null' \  
> /usr/local/bin/start-asdm \  
&& chmod +x /usr/local/bin/start-asdm \  
#  
# startup script  
#  
&& sed -i '/firefox/d' /etc/init.sh  
  
VOLUME [ "/etc/java-8-openjdk" ]  

