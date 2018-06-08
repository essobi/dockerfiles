FROM ginseadd/ssb  
# TODO: switch the order - ssb should inherit from electron, so that electron
is more universally useful  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gconf2 \  
gconf-service \  
gvfs-bin \  
libasound2 \  
libcap2 \  
libgconf-2-4 \  
libgnome-keyring-dev \  
libgtk2.0-0 \  
libnotify4 \  
libnss3 \  
libxkbfile1 \  
libxss1 \  
libxtst6 \  
libx11-xcb-dev \  
xdg-utils  
  
WORKDIR /root  
  
# TODO: add npm packages that are common between patchwork and patchbay  
# after npm install  
# fix some errors with leveldown  
#RUN npm install electron-rebuild && ./node_modules/.bin/electron-rebuild  
# cleanup ?  
#RUN apt-get clean && apt-get purge --auto-remove -y curl git \  
# && rm -rf /var/lib/apt/lists/*  

