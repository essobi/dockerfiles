FROM ubuntu:latest  
  
# Dependencies for the download assistant  
RUN apt-get update && apt-get install -y \  
libgtk2.0-0 \  
libsoup2.4-1 \  
libarchive13 \  
libpng16-16 \  
libgconf-2-4  
  
ADD https://beta.unity3d.com/download/aea5ecb8f9fd/UnitySetup-2017.3.1f1 \  
unity-installer  
RUN chmod +x unity-installer  
  
RUN yes | ./unity-installer --unattended \  
\--components=Unity \  
\--install-location=/opt/unity  
  
# Dependencies for the editor.  
# We install these afterwards, so that we have to rebuild less layers if a  
# dependency changes.  
RUN apt-get install -y \  
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
npm \  
# 'Fake' X server for running headless  
xvfb  
  

