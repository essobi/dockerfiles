########################################################################  
# hub.docker.com/r/gruen/stylus/  
# Stylus task runner  
#  
# Usage  
# docker run --it -rm \  
# -v [path/to/source/files]:/inputfiles \  
# -v [path/to/build/files]:/outputfiles \  
# --name stylus"$(date +%N) \  
# gruen/stylus \  
# [stylus options] /inputfiles/[main.styl] \  
# -o /outputfiles/[style.css]  
#  
########################################################################  
FROM alpine:3.3  
LABEL maintainer "Darren Green <darren@gruen.site>"  
RUN apk \  
\--no-cache \  
\--progress \  
\--update \  
add nodejs \  
&& npm install stylus -g \  
&& mkdir /inputfiles /outputfiles  
VOLUME ["/inputfiles", "/outputfiles"]  
ENTRYPOINT ["stylus"]  

