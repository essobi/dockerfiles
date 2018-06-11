FROM ubuntu:16.04  
  
ENV unityFile=unity-editor-5.4.2f2+20161111_amd64.deb  
# ENV unityFile=unity-editor-5.4.3f1-3+20161125_amd64.deb  
ENV androidSdkFile=tools_r25.2.2-linux.zip  
  
# This is necessary for unity  
ENV ANDROID_SDK_ROOT=/usr/local/androidSdk/  
# Download necessary packages for unity3d  
RUN apt-get update -qq; \  
apt-get install -qq -y \  
busybox-static \  
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
lib32z1 \  
nano \  
openjdk-8-jdk \  
screen \  
unzip \  
zlib1g \  
debconf \  
npm \  
xdg-utils \  
lsb-release \  
libpq5 \  
xvfb \  
wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# ADD unity3d to system  
RUN wget -nv http://download.unity3d.com/download_unity/linux/${unityFile}; \  
dpkg -i ${unityFile}; \  
rm ${unityFile};  
  
# Prepare directories for unity3d:  
RUN mkdir -p $HOME/.local/share/unity3d/Unity; \  
mkdir -p $HOME/.cache/unity3d;  
  
# über folgenden Befehl koennte man in der Zukunft die license-File aus dem
Docker-Repo direkt einspielen:  
# ADD Unity_v5.x.ulf $HOME/.local/share/unity3d/Unity/  
# Install Androidsdk with build tools for android-23:  
RUN mkdir -p $ANDROID_SDK_ROOT; \  
wget -nv https://dl.google.com/android/repository/${androidSdkFile}; \  
unzip ${androidSdkFile} -d $ANDROID_SDK_ROOT; \  
( sleep 5 && while [ 1 ]; do sleep 1; echo y; done ) \  
| $ANDROID_SDK_ROOT/tools/android update sdk --no-ui --all --filter
tool,platform-tool,android-23,build-tools-23.0.2; \  
rm ${androidSdkFile};  
  
# Clean up  
RUN rm -rf /tmp/* /var/tmp/*  

