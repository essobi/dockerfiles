FROM debian:stable  
  
RUN apt-get update && apt-get install -y \  
libgtk2.0-0 \  
libsoup2.4-1 \  
libarchive13 \  
libglu1-mesa \  
libpng-dev  
  
ADD http://beta.unity3d.com/download/3c89f8d277f5/UnitySetup-2017.3.0f1 .  
# run the setup, echo y accepts the unity license since there's no command
flag to do it  
RUN chmod +x UnitySetup-2017.3.0f1; sync; echo y | ./UnitySetup-2017.3.0f1
--unattended --install-location=/opt/unity  

