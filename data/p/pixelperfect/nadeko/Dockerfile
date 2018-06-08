FROM ubuntu:16.04  
MAINTAINER PixelPerfect <pixelperfectpon3@gmail.com>  
  
WORKDIR /opt/  
  
# Installing Dependencies  
RUN apt update -y  
RUN apt upgrade -y  
RUN apt dist-upgrade -y  
RUN apt-get install software-properties-common apt-transport-https wget curl
sudo -y  
RUN wget http://launchpadlibrarian.net/201330288/libicu52_52.1-8_amd64.deb  
RUN dpkg -i /opt/libicu52_52.1-8_amd64.deb  
RUN rm -rf /opt/libicu52_52.1-8_amd64.deb  
RUN add-apt-repository ppa:jonathonf/ffmpeg-3 -y  
RUN add-apt-repository ppa:nilarimogard/webupd8 -y  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg  
RUN sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
RUN sudo sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main"
> /etc/apt/sources.list.d/dotnetdev.list'  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893  
RUN apt update -y  
RUN apt upgrade -y  
RUN apt dist-upgrade -y  
RUN apt install git -y  
RUN apt install dotnet-sdk-2.0.0 libopus0 opus-tools libopus-dev libsodium-dev
ffmpeg tmux youtube-dl dotnet-sharedframework-microsoft.netcore.app-1.1.2
dotnet-sharedframework-microsoft.netcore.app-1.0.5 libicu52 python
python3.5-dev redis-server -y  
  
#Download and install stable version of Nadeko  
RUN curl -L
https://raw.githubusercontent.com/iPonyRadio/nadeko/1.10/nadeko_installer.sh |
sh \  
&& curl -L
https://raw.githubusercontent.com/iPonyRadio/nadeko/1.10/nadeko_autorestart.sh
> nadeko.sh \  
&& chmod 755 nadeko.sh  
  
VOLUME ["/root/nadeko"]  
  
CMD ["/opt/nadeko.sh"]  

