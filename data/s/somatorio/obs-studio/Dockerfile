FROM ubuntu:16.04  
  
RUN echo "deb http://archive.ubuntu.com/ubuntu/ xenial multiverse" >>
/etc/apt/sources.list.d/multiverse.list && \  
echo "deb http://ppa.launchpad.net/obsproject/obs-studio/ubuntu xenial main"
>> /etc/apt/sources.list.d/obs.list && \  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys
BC7345F522079769F5BBE987EFC71127F425E228 && \  
apt-get update && apt-get install -y libfdk-aac0 ffmpeg obs-studio --no-
install-recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENTRYPOINT ["/usr/bin/obs"]  

