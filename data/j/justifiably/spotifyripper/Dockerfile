FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Use local copy  
#
https://developer.spotify.com/download/libspotify/libspotify-12.1.51-Linux-x86_64-release.tar.gz  
ADD libspotify-12.1.51-Linux-x86_64-release.tar.gz /tmp/  
  
# Codecs: lame, flac, vorbis to support mp3, flac, ogg  
RUN apt-get update && \  
apt-get install -y build-essential python python-pkg-resources git libffi-dev
python-pip python-dev \  
lame flac vorbis-tools && \  
cd /tmp/libspotify-12.1.51-Linux-x86_64-release && \  
make install prefix=/usr/local && \  
cd /tmp && git clone https://github.com/ElectryDev/spotify-ripper.git && \  
pip install --upgrade pip && \  
cd spotify-ripper && pip install --upgrade . && \  
apt-get remove -y build-essential git libffi-dev python-pip python-dev && \  
apt-get autoremove -y && apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
# Set up local user to run as  
RUN useradd -u 1001 -ms /bin/bash spotifyripper  
  
USER spotifyripper  
ENV HOME /home/spotifyripper  
RUN mkdir /home/spotifyripper/music /home/spotifyripper/.spotify-ripper  
  
WORKDIR /home/spotifyripper/music  
VOLUME ["/home/spotifyripper/.spotify-ripper", "/home/spotifyripper/music"]  
  
ENTRYPOINT ["/usr/local/bin/spotify-ripper"]  
  

