# Run Opticks in a container  
#  
# docker run -i -t \  
# -v $HOME/Data:/home/data \ <\- mounts data directory to container  
# toddstavish/opticks  
#  
# GUI Dependencies: Linux -> -v /tmp/.X11-unix:/tmp/.X11-unix and -e
DISPLAY=unix$DISPLAY  
# OSX -> XQuartz and  
# socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\" and  
# -e DISPLAY=192.168.99.1:0 <\- this the default virtualbox ip address  
#  
FROM ubuntu:15.04  
MAINTAINER Todd Stavish <toddstavish@gmail.com>  
  
# Download Opticks  
ADD http://opticks.org/downloads/opticks/4.12.0/opticks_4.12.0-1_amd64.deb
/tmp/opticks_4.12.0-1_amd64.deb  
  
# Install Opticks  
RUN apt-get update && apt-get install -y \  
libtbb2 \  
libpq5 \  
libglu1 \  
libxmu6 \  
libxi6 \  
libglib2.0-0 \  
libfreetype6 \  
libxrender1 \  
libgl1-mesa-dri \  
\--no-install-recommends  
  
RUN dpkg -i /tmp/opticks_4.12.0-1_amd64.deb && \  
rm /tmp/opticks_4.12.0-1_amd64.deb && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/opt/Opticks/Bin/Opticks"]  

