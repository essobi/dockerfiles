  
FROM debian:jessie-slim  
RUN apt-get update && apt-get install -y \  
libc6 \  
libdbus-1-3 \  
libqt5gui5 \  
libqt5widgets5 \  
libqt5qml5 \  
libqt5quick5 \  
libqt5dbus5 \  
libqt5webkit5 \  
libqt5x11extras5 \  
qml-module-qtgraphicaleffects \  
qml-module-qtquick2 \  
qml-module-qtquick-controls \  
qml-module-qtquick-dialogs \  
qml-module-qtquick-window2 \  
qml-module-qtquick-layouts \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
RUN buildDeps=' \  
ca-certificates \  
curl \  
' \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \  
&& curl -L https://download.teamviewer.com/download/teamviewer_amd64.deb >
/tmp/teamviewer.deb \  
RUN dpkg -i /tmp/teamviewer.deb \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -r /tmp/*.deb \  
&& apt-get purge -y --auto-remove $buildDeps  
ENTRYPOINT [ "teamviewer" ]  

