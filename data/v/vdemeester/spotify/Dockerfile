## -*- docker-image-name: "vdemeester/spotify" -*-  
# Run spotify in a container  
# docker run -ti --rm \  
# -v /etc/localtime:/etc/localtime:ro \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=unix$DISPLAY \  
# -v /run/user/1000/pulse/native:/run/pulse/socket \  
# -e PULSE_SERVER=unix:/run/pulse/socket \  
# -v ~/.config/pulse/cookie:/run/pulse/cookie \  
# -e PULSE_COOKIE=/run/pulse/cookie \  
# -v /var/run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket \  
# -v $HOME/.spotify/config:/home/spotify/.config/spotify \  
# -v $HOME/.spotify/cache:/home/spotify/cache \  
# --name spotify \  
# vdemeester/spotify  
FROM ubuntu:14.04  
MAINTAINER Jessie Frazelle <jess@linux.com>  
MAINTAINER Vincent Demeester <vincent@sbr.pm>  
  
RUN apt-get update && apt-get install -y \  
libpangoxft-1.0-0 \  
alsa-utils \  
software-properties-common \  
pulseaudio \  
\--no-install-recommends && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 94558F59 && \  
echo "deb http://repository.spotify.com stable non-free" >>
/etc/apt/sources.list.d/spotify.list && \  
apt-get update && \  
apt-get install --force-yes -y \  
spotify-client \  
&& rm -rf /var/lib/apt/lists/*  
  
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

