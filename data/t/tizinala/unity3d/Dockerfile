FROM ubuntu  
  
# http://forum.unity3d.com/threads/unity-on-linux-release-notes-and-known-
issues.350256/  
  
RUN apt-get update && apt-get install -y \  
gconf-service \  
lib32gcc1 \  
lib32stdc++6 \  
libasound2 \  
libc6 \  
libc6-i386 \  
libcairo2 \  
libcap2 \  
libcups2 \  
libdbus-1-3 \  
libexpat1 \  
libfontconfig1 \  
libfreetype6 \  
libgcc1 \  
libgconf-2-4 \  
libgdk-pixbuf2.0-0 \  
libgl1-mesa-glx \  
libglib2.0-0 \  
libglu1-mesa \  
libgtk2.0-0 \  
libnspr4 \  
libnss3 \  
libpango1.0-0 \  
libstdc++6 \  
libx11-6 \  
libxcomposite1 \  
libxcursor1 \  
libxdamage1 \  
libxext6 \  
libxfixes3 \  
libxi6 \  
libxrandr2 \  
libxrender1 \  
libxtst6 \  
zlib1g \  
debconf \  
psmisc \  
npm \  
xdg-utils \  
lsb-release \  
libpq5 \  
wget \  
xvfb \  
libgtk2.0-dev libsoup2.4-dev libarchive-dev libpng-dev  
  
RUN wget -O /tmp/installer
http://beta.unity3d.com/download/3c89f8d277f5/UnitySetup-2017.3.0f1 && mkdir
-p /unity && chmod 755 /tmp/installer  
# RUN yes | /tmp/installer --unattended --components=Unity --install-
location=/unity  
RUN yes | /tmp/installer --unattended
--components=Unity,Android,iOS,Mac,WebGL,Windows --install-location=/unity  
  
# RUN wget -O /tmp/unity.deb
http://beta.unity3d.com/download/ddd95e743b51/unity-
editor_amd64-5.6.2xf1Linux.deb && dpkg -i /tmp/unity.deb && rm /tmp/unity.deb  
# unity: /unity/Editor/Unity  

