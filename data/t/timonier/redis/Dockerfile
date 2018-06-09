FROM redis:alpine  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add \--no-cache --no-progress \  
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
-s -- install  
  
ENTRYPOINT [ "dumb-entrypoint" , "docker-entrypoint.sh" ]  

