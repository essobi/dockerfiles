FROM ubuntu:artful  
MAINTAINER Max Schmitt, xeetsh@xeet.sh  
  
RUN apt-get -qq update && apt-get -qq install -y \  
libgtk2.0-0 libsoup2.4-1 libarchive13 libpng16-16 wget gconf-service \  
lib32gcc1 lib32stdc++6 libasound2 libc6 libc6-i386 libcairo2 \  
libcap2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libfreetype6 \  
libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libgl1-mesa-glx libglib2.0-0 \  
libglu1-mesa libgtk2.0-0 libnspr4 libnss3 libpango1.0-0 libstdc++6 \  
libx11-6 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 \  
libxrandr2 libxrender1 libxtst6 zlib1g debconf psmisc npm xdg-utils \  
lsb-release libpq5 wget xvfb  
  
RUN wget http://beta.unity3d.com/download/3c89f8d277f5/UnitySetup-2017.3.0f1  
RUN chmod +x UnitySetup-2017.3.0f1  
RUN mkdir /opt/unity3d  
RUN yes | ./UnitySetup-2017.3.0f1 --unattended
--components=Unity,Android,iOS,Mac,WebGL,Windows --install-
location=/opt/unity3d  
RUN ln -s /opt/unity3d/Editor/Unity /usr/local/bin/unity-editor  

