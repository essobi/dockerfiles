FROM ginseadd/electron  
  
# Run as:  
# docker run --rm -it -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY
patchwork npm start  
# this might be also needed for sound, if there is any...  
# --device /dev/snd  
#  
# I also had to run `xhost local:docker` on my host computer, to allow docker
using my X server (get rid of "No protocol specified")  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
libxext-dev libx11-xcb-dev  
# libxtst-dev libxkbfile-dev  
RUN git clone https://github.com/ssbc/patchwork  
WORKDIR /root/patchwork  
RUN npm install  
  
# fix some errors with leveldown  
RUN npm install electron-rebuild && ./node_modules/.bin/electron-rebuild  
  
# cleanup  
RUN apt-get clean && apt-get purge --auto-remove -y curl git \  
&& rm -rf /var/lib/apt/lists/*  

