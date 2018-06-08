# billygoat/video-transcoding:0.16.0  
FROM ntodd/ruby-xenial:2.3.1  
MAINTAINER Billy Mabray  
  
RUN apt-get update -qq && apt-get install -y software-properties-common  
RUN add-apt-repository ppa:stebbins/handbrake-releases  
  
# Install dependencies  
RUN apt-get update -qq && apt-get install -y \  
ffmpeg \  
mkvtoolnix \  
mp4v2-utils \  
mplayer \  
handbrake-cli  
  
# Install video_transcoding gem  
RUN gem install video_transcoding  
  
# Compile tivodecode and tdcat, install to /usr/local/bin/ (pyTivo will be
able to find this automatically)  
RUN apt-get install -qy build-essential  
RUN wget
http://sourceforge.net/projects/tivodecode/files/tivodecode/0.2pre4/tivodecode-0.2pre4.tar.gz  
RUN tar xvfz tivodecode-0.2pre4.tar.gz -C /opt/  
RUN cd /opt/tivodecode-0.2pre4;./configure  
RUN cd /opt/tivodecode-0.2pre4;make  
RUN cd /opt/tivodecode-0.2pre4;make install  
  
# Set work directory  
RUN mkdir /data  
WORKDIR /data  
  
CMD [ "/bin/bash" ]  

