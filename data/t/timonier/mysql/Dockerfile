FROM mysql:latest  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
RUN set -ex \  
\  
# Prepare system  
\  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
\  
# Install packages  
\  
&& apt-get install --no-install-recommends --yes \  
ca-certificates \  
curl \  
\  
# Install timonier/dumb-entrypoint  
\  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/dumb-entrypoint/installer" |
INSTALL_DIRECTORY="/usr/sbin" sh -s -- install \  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/gosu/installer" | INSTALL_DIRECTORY="/usr/sbin" sh
-s -- install \  
\  
# Clean  
\  
&& rm --force --recursive \  
/tmp/* \  
/var/lib/apt/lists/*  
  
ENTRYPOINT [ "dumb-entrypoint" , "docker-entrypoint.sh" ]  

