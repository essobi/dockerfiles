FROM ubuntu:latest  
  
#Install Dependencies  
RUN apt-get update && apt-get install -y \  
curl \  
python \  
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
libsoup2.4-1 \  
libarchive13 \  
libpng-dev \  
zlib1g \  
debconf \  
npm \  
ffmpeg \  
nodejs \  
openjdk-8-jdk \  
gzip \  
xvfb  
  
#Download Unity  
RUN curl -o /root/UnitySetup
https://beta.unity3d.com/download/170f0691b973/UnitySetup-2018.1.0f2 && \  
chmod +x /root/UnitySetup  
  
#Install Unity  
RUN printf 'y\n' | /root/UnitySetup --unattended --components=Unity,Windows-
Mono,WebGL --install-location=/opt/Unity  
RUN rm /root/UnitySetup  
  
#Create Unity Directories  
RUN mkdir -p /root/.cache/unity3d && mkdir -p /root/.local/share/unity3d/Unity
&& mkdir -p /root/.local/share/unity3d/Certificates  
  
#Activate Unity  
ADD License/Unity_lic.ulf /root/.local/share/unity3d/Unity/Unity_lic.ulf  
ADD License/CACerts.pem /root/.local/share/unity3d/Certificates/CACerts.pem  
  
#Add Scripts  
ADD Script/UnityBuild /opt/Unity/Editor/UnityBuild  
RUN chmod +x /opt/Unity/Editor/UnityBuild  
  
#Add Unity to Path  
ENV PATH="${PATH}:/opt/Unity/Editor"  

