FROM ubuntu:latest  
MAINTAINER Carson Longhorn <dockerfiles@unrelated.net.au>  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install \  
software-properties-common \  
&& \  
add-apt-repository ppa:stebbins/handbrake-releases && \  
apt-get update && \  
apt-get -y install \  
ffmpeg \  
frei0r-plugins \  
gawk \  
handbrake-cli \  
mediainfo \  
mencoder \  
mkvtoolnix \  
mp4v2-utils \  
mplayer \  
rename \  
ruby \  
sshfs \  
&& \  
apt-get clean && \  
rm -rf /var/cache/* /var/log/apt/* /tmp/* && \  
gem install video_transcoding && \  
echo Finished > /dev/null  
COPY content/running_notes.txt /root/running_notes.txt  
CMD /bin/bash  

