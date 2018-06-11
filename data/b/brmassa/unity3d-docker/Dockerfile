FROM ubuntu  
  
# install system dependencies  
RUN apt-get -qq update && apt-get -qq install -y \  
curl gconf-service lib32gcc1 lib32stdc++6 libasound2 libc6 libc6-i386
libcairo2 libcap2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libfreetype6
libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libgl1-mesa-glx libglib2.0-0
libglu1-mesa libgtk2.0-0 libnspr4 libnss3 libpango1.0-0 libstdc++6 libx11-6
libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2
libxrender1 libxtst6 zlib1g debconf npm xdg-utils lsb-release libpq5 xvfb \  
&& rm -rf /var/lib/apt/lists/*  
  
# use script to download Unity from the official site  
ADD unity-versions.sh /app/unity-versions.sh  
RUN chmod +x /app/unity-versions.sh  
ADD unity-download.sh /app/unity-download.sh  
RUN chmod +x /app/unity-download.sh  
RUN ["/bin/bash", "-c", "/app/unity-download.sh UNITY_5_6_0_F3"]  
  
# install Unity3D  
RUN mkdir -p /root/.cache/unity3d && mkdir -p /root/.local/share/unity3d  
RUN dpkg -i /app/unity_editor.deb && rm /app/unity_editor.deb  
  
# utility to make easier to use Unity3D  
ADD unity-docker.sh /usr/local/bin/unity-docker.sh  
RUN chmod +x /usr/local/bin/unity-docker.sh  

