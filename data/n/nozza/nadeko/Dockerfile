FROM phusion/baseimage:latest  
  
WORKDIR /opt/  
  
# Install Dotnet  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor >
microsoft.gpg  
RUN mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg  
RUN sh -c 'echo "deb [arch=amd64]
https://packages.microsoft.com/repos/microsoft-ubuntu-xenial-prod xenial main"
> /etc/apt/sources.list.d/dotnetdev.list'  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893  
  
# Add ffmpeg3 ppa  
RUN add-apt-repository ppa:jonathonf/ffmpeg-3  
  
# Install required software  
RUN apt-get update && apt-get install -y git libopus0 opus-tools libopus-dev
libsodium-dev ffmpeg tmux rsync python dotnet-sdk-2.0.0 redis-server tzdata  
  
#Add youtube-dl  
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o
/usr/local/bin/youtube-dl && chmod a+rx /usr/local/bin/youtube-dl  
  
#Download and install stable version of Nadeko  
RUN curl -O https://raw.githubusercontent.com/Nozza-
VS/nadeko/latest/nadeko_installer.sh && chmod 755 nadeko_installer.sh &&
./nadeko_installer.sh \  
&& curl -O https://raw.githubusercontent.com/Nozza-
VS/nadeko/latest/nadeko_autorestart.sh && chmod 755 nadeko_autorestart.sh  
  
# Set a default timezone  
#RUN echo "Australia/Brisbane" | tee /etc/timezone  
#RUN ln -sf /usr/share/zoneinfo/Australia/Brisbane /etc/localtime  
VOLUME ["/root/nadeko"]  
  
CMD ["sh","/opt/nadeko_autorestart.sh"]  

