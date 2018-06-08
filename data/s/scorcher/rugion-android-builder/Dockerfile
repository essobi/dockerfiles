FROM scorcher/rugion-android-base:latest  
  
MAINTAINER Nikolay Didenko "nd@info74.ru"  
# Create emulator  
RUN echo "no" | android create avd \  
\--force \  
\--device "Nexus 5" \  
\--name test \  
\--target android-21 \  
\--abi armeabi-v7a \  
\--skin WVGA800 \  
\--sdcard 512M  
  
# GO to workspace  
WORKDIR /opt/workspace  

