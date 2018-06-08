FROM debian:jessie  
  
# Install dependencies  
RUN apt-get update && apt-get install -y \  
libgl1-mesa-swx11 \  
sudo \  
wget \  
xvfb  
  
# Install Haxe  
RUN wget -qO /tmp/haxe.tar.gz
http://www.openfl.org/builds/haxe/haxe-3.2.1-linux-installer.tar.gz && \  
tar xzf /tmp/haxe.tar.gz -C /tmp && \  
/tmp/install-haxe.sh -y  
  
# Install HaxeFlixel  
RUN haxelib install flixel  

