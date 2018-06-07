# run gnucash in a container  
#  
# docker run -it \  
# \--net host \  
# \--cpuset-cpus 0 \  
# \--memory 512mb \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \ # mount the X11 socket  
# -e DISPLAY=unix$DISPLAY \  
# -v /dev/shm:/dev/shm \  
# -v gnucash:/home/gnucash \ # save changes in /home/gnucash  
# \--name gnucash  
# kailemke/gnucash  
  
# base image  
FROM debian:stretch  
LABEL maintainer "Kai Lemke <kai.lemke91@gmx.de>"  
  
# install gnucash etc.  
RUN apt-get update && apt-get install -y \  
gnucash \  
gnucash-docs \  
yelp \  
libdbd-mysql \  
dbus-x11 \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  
  
RUN groupadd gnucash \  
&& useradd -g gnucash -G video gnucash -m  
  
# run gnucash as non-privileged user  
USER gnucash  
  
# autorun gnucash  
ENTRYPOINT [ "gnucash" ]  
# ENTRYPOINT [ "bash" ]  

