# Download Ubuntu base image from phusion  
# https://github.com/phusion/baseimage-docker  
FROM phusion/baseimage:latest  
  
# Define working directory  
WORKDIR /opt/  
  
# Prepare for Basic stuff  
RUN apt-get update  
RUN apt-get install software-properties-common apt-transport-https curl -y  
  
# Register the trusted Microsoft signature key  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg  
RUN mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
  
# Register the Microsoft Product feed for your distro version  
RUN sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main"
> /etc/apt/sources.list.d/dotnetdev.list'  
  
# Add ffmpeg3 ppa  
RUN add-apt-repository ppa:jonathonf/ffmpeg-3  
  
# Updating existing tools  
RUN apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y  
  
# Install Git  
RUN apt-get update && apt-get install -y git  
  
# Install .Net Core  
RUN apt-get update && apt-get install -y dotnet-sdk-2.0.0  
  
# Install Redis-server  
RUN apt-get update && apt-get install -y redis-server  
  
# Install required software  
RUN apt-get update && apt-get install -y libopus0 opus-tools libopus-dev
libsodium-dev ffmpeg rsync python python3-pip tzdata  
  
#Add youtube-dl  
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o
/usr/local/bin/youtube-dl && chmod a+rx /usr/local/bin/youtube-dl  
  
#Download and install stable version of Nadeko  
RUN curl -H "Cache-Control: no-cache"
https://raw.githubusercontent.com/willysunny/Nadecker/master/nadeko_installer_2_22_0.sh
-o ./nadeko_installer.sh && chmod 755 nadeko_installer.sh &&
./nadeko_installer.sh  
RUN curl -O -H "Cache-Control: no-cache"
https://raw.githubusercontent.com/willysunny/Nadecker/master/nadeko_autorestart.sh
&& chmod 755 nadeko_autorestart.sh  
  
VOLUME ["/root/nadeko"]  
  
CMD ["sh","/opt/nadeko_autorestart.sh"]  

