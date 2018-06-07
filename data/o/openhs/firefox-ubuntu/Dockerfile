# Dockerfile  
#  
# Project: docker-firefox-ubuntu  
# License: GNU GPLv3  
#  
# Copyright (C) 2015 - 2018 Robert Cernansky  
FROM openhs/ubuntu-nvidia  
  
  
  
MAINTAINER openhs  
LABEL version = "0.5.0" \  
description = "Firefox with Flash and nVidia graphics driver."  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
firefox \  
flashplugin-installer \  
unzip \  
ca-certificates  
  
# Firefox addons which shall be installed (NoScript Security Suite, Cookie
AutoDelete, Disconnect, Proxy Switcher and Manager); the  
# format is '<addon_number:addon_id> [...]' where 'addon_number' identifies
addon for downloading and 'addon_id' is  
# identifier for installation  
ARG addons="722:{73a6fe31-595d-460b-a920-fcc0f8843232}
860751:CookieAutoDelete@kennydo.com 464050:2.0@disconnect.me
840875:{e4a12b8a-ab12-449a-b70e-4f54ccaf235e}"  
RUN profile=docker.default && \  
addonsDir=/home/appuser/.mozilla/firefox/${profile}/extensions && \  
\  
mkdir -p ${addonsDir} && \  
\  
/bin/echo -e \  
"[General]\n\  
StartWithLastProfile=1\n\  
\n\  
[Profile0]\n\  
Name=default\n\  
IsRelative=1\n\  
Path=${profile}\n\  
Default=1" >> /home/appuser/.mozilla/firefox/profiles.ini && \  
\  
downloadAddon() { \  
wget
https://addons.mozilla.org/firefox/downloads/file/${1}/addon-${1}-latest.xpi
|| \  
wget
https://addons.mozilla.org/firefox/downloads/latest/${1}/addon-${1}-latest.xpi
|| \  
wget
https://addons.mozilla.org/firefox/downloads/latest/${1}/platform:2/addon-${1}-latest.xpi;
\  
} && \  
\  
addonNum() { \  
echo ${1%:*}; \  
} && \  
\  
addonId() { \  
echo ${1#*:}; \  
} && \  
\  
for addon in ${addons}; do \  
addonNum=$(addonNum ${addon}) && \  
downloadAddon ${addonNum} && \  
mv addon-${addonNum}-latest.xpi ${addonsDir}/$(addonId ${addon}).xpi; \  
done && \  
chown -R appuser:appuser /home/appuser/.mozilla  
  
COPY container_startup.sh /opt/  
RUN chmod +x /opt/container_startup.sh  
  
ENTRYPOINT ["/opt/container_startup.sh"]  

