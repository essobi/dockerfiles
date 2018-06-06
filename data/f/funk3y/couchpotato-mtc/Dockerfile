FROM linuxserver/couchpotato  
MAINTAINER FuN_KeY  
  
  
# install app  
RUN \  
apk add --no-cache mkvtoolnix && \  
dest='/etc/cont-init.d/20-mtc' && \  
printf $'#!/usr/bin/with-contenv bash\nsu -s \'/bin/bash\' -c
\'dest="/config/data/custom_plugins/MkvTracksCleanup" && rm -rf $dest && git
clone \--depth=1 https://github.com/FuNK3Y/MkvTracksCleanup.git $dest\' abc' >
$dest && \  
chmod +x $dest  
  
VOLUME /cleanup  

