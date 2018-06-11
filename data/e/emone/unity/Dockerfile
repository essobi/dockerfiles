FROM ubuntu  
  
# alter this when you need to bump the Unity version. Pick a version from  
# http://forum.unity3d.com/threads/unity-on-linux-release-notes-and-known-
issues.350256/  
# Change link + filename in "UPDATE IF NECESSARY" below  
  
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
npm \  
xdg-utils \  
lsb-release \  
libpq5 \  
xvfb \  
wget  
  
# UPDATE IF NECESSARY  
ENV UNITY_URL http://beta.unity3d.com/download/ddd95e743b51/unity-editor-
installer-5.6.2xf1Linux.sh  
ENV UNITY_FNAME unity-editor-installer-5.6.2xf1Linux.sh  
  
# Download, extract and remove installer  
# Then move the extracted folder where it will be expected  
RUN wget --progress=dot:giga "$UNITY_URL" && \  
sh $UNITY_FNAME && rm $UNITY_FNAME && \  
mkdir -p /opt && \  
mv unity-editor-5.6.2xf1Linux /opt/Unity  

