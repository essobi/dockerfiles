FROM debian:stretch-slim  
  
LABEL maintainer="Max Schmitt <max@schmitt.mx>"  
LABEL maintainer="Yannick Schinko <yannick@tedworld.de>"  
LABEL description="Docker Image for the Teamspeak 3 and Discord MusicBot
called SinusBot customized to work with Pterodactyl."  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends ca-certificates bzip2 wget less
x11vnc xvfb libxcursor1 libnss3 libegl1-mesa libasound2 libglib2.0-0 python
libxcomposite-dev && \  
apt-get -q clean all && \  
rm -rf /tmp/* /var/tmp/* && \  
adduser --disabled-password --home /home/container container  
  
WORKDIR /opt/sinusbot  
  
COPY ./install.sh ./install.sh  
  
# Download/Install TeamSpeak Client  
RUN bash install.sh teamspeak  
  
# Download/Install youtube-dl  
RUN bash install.sh youtube-dl  
  
USER container  
ENV USER=container HOME=/home/container  
  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
  
CMD ["/bin/bash", "/entrypoint.sh"]  

