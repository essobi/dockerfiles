FROM fedora:latest  
MAINTAINER Sudarsha Hewa <sudarsha@gamil.com>  
  
RUN dnf install -y openconnect vpnc-script git \  
firefox curl dbus-x11 \  
remmina-plugins-rdp \  
mozilla-fira-mono-fonts mozilla-fira-sans-fonts \  
mozilla-fira-fonts-common \  
dejavu-fonts-common dejavu-sans-fonts dejavu-sans-mono-fonts \  
dejavu-serif-fonts fontawesome-fonts fontawesome-fonts-web \  
gdouros-symbola-fonts gnu-free-fonts-common \  
gnu-free-mono-fonts gnu-free-sans-fonts gnu-free-serif-fonts \  
monofett-fonts overpass-mono-fonts \  
oxygen-fonts-common oxygen-mono-fonts pcaro-hermit-fonts \  
&& echo "Settingg up google chorme browser ..." \  
&& curl -LO --silent https://dl.google.com/linux/direct/google-chrome-
stable_current_x86_64.rpm \  
&& dnf localinstall -y google-chrome-stable_current_x86_64.rpm \  
&& rm -f google-chrome-stable_current_x86_64.rpm  

