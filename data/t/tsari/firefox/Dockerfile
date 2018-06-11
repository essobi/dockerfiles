# !/bin/bash  
# xhost +local:docker && \  
# docker run -it \  
# --env="USER" \  
# --env="UID=$(id -u)" \  
# --env="GID=$(id -g)" \  
# --env="HOME" \  
# --volume="/home/$USER:/home/$USER" \  
# --env="DISPLAY" \  
# -v /dev/snd:/dev/snd \  
# --device /dev/snd \  
# -v /var/lib/dbus:/var/lib/dbus:ro \  
# -v /dev/shm:/dev/shm \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# --net="host" \  
# tsari/firefox  
FROM tsari/docker-desktop-base  
MAINTAINER Tibor Sári <tiborsari@gmx.de>  
  
# Setting the Firefox version and installation directory through environment
variables.  
ENV FIREFOX_VERSION 46.0  
ENV FIREFOX_DIR $HOME/firefox  
ENV FIREFOX_FILENAME $FIREFOX_DIR/firefox.tar.bz2  
ENV FIREFOX_LANGUAGE de  
  
# Create the Firefox directory, download the custom Firefox version from
Mozilla and untar it.  
RUN mkdir $FIREFOX_DIR  
RUN wget -q --continue \--output-document $FIREFOX_FILENAME
"https://ftp.mozilla.org/pub/mozilla.org/firefox/releases/${FIREFOX_VERSION}/linux-x86_64/${FIREFOX_LANGUAGE}/firefox-${FIREFOX_VERSION}.tar.bz2"  
RUN tar -xaf "$FIREFOX_FILENAME" \--strip-components=1 --directory
"$FIREFOX_DIR" \  
&& ln -s $FIREFOX_DIR/firefox /usr/local/bin/firefox  
  
CMD ["firefox"]

