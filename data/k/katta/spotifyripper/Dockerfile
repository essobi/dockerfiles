FROM ubuntu:16.04  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
# Codecs: lame, flac, vorbis to support mp3, flac, ogg  
RUN apt-get -qq update && \  
apt-get -qq install -y curl apt-transport-https && \  
curl -sL http://apt.mopidy.com/mopidy.gpg | apt-key add \- && \  
echo deb http://apt.mopidy.com/ stable main contrib non-free >
/etc/apt/sources.list.d/mopidy.list && \  
apt-get -qq update && \  
apt-get -qq install -y libspotify12 libspotify-dev python python-pkg-resources
libffi-dev python-pip python-dev lame flac vorbis-tools && \  
mkdir /usr/src/spotify-ripper && \  
curl -sL https://api.github.com/repos/SolidHal/spotify-ripper/tarball | tar xz
-C /usr/src/spotify-ripper --strip-components=1 && \  
pip install --upgrade pip && \  
cd /usr/src/spotify-ripper && pip install --upgrade . && \  
apt-get -qq --purge autoremove -y libffi-dev python-pip python-dev libspotify-
dev curl apt-transport-https apt-transport-https && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/mopidy.list && \  
rm -rf /tmp/* /usr/src/spotify-ripper  
  
# Set up local user to run as  
RUN useradd -u 1001 -ms /bin/bash spotifyripper  
  
USER spotifyripper  
ENV HOME /home/spotifyripper  
RUN mkdir /home/spotifyripper/music /home/spotifyripper/.spotify-ripper  
  
WORKDIR /home/spotifyripper/music  
VOLUME ["/home/spotifyripper/.spotify-ripper", "/home/spotifyripper/music"]  
  
ENTRYPOINT ["/usr/local/bin/spotify-ripper"]  

