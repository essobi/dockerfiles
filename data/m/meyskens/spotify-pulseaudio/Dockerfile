FROM meyskens/desktop-base  
  
RUN echo "deb http://ftp.de.debian.org/debian jessie main " >>
/etc/apt/sources.list.d/workaround.list  
  
RUN apt-get update && apt-get install -y \  
libpangoxft-1.0-0 \  
alsa-utils \  
software-properties-common \  
pulseaudio \  
libgl1-mesa-dri \  
libgl1-mesa-glx \  
libpangoxft-1.0-0 \  
libssl1.0.0 \  
libssl1.0.2 \  
libxss1 \  
\--no-install-recommends && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
BBEBDCB318AD50EC6865090613B00F1FD2C19886 && \  
echo "deb http://repository.spotify.com stable non-free" >>
/etc/apt/sources.list.d/spotify.list && \  
apt-get update && \  
apt-get install -y spotify-client && \  
rm -rf /var/lib/apt/lists/*  
  
ENV HOME /home/spotify  
RUN useradd --create-home --home-dir $HOME spotify \  
&& gpasswd -a spotify audio \  
&& chown -R spotify:spotify $HOME  
  
WORKDIR $HOME  
USER spotify  
  
# make search bar text better  
RUN echo "QLineEdit { color: #000 }" > /home/spotify/spotify-override.css  
  
ENTRYPOINT [ "spotify" ]  
CMD [ "-stylesheet=/home/spotify/spotify-override.css" ]

