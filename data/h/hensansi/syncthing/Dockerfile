From alpine:3.5  
ENV SYNCTHING_VERSION=0.14.36  
RUN apk update && apk add --no-cache curl \  
&& tarball="syncthing-linux-amd64-v${SYNCTHING_VERSION}.tar.gz" \  
&& echo
"https://github.com/syncthing/syncthing/releases/download/v${SYNCTHING_VERSION}/${tarball}"
\  
&& curl -L
"https://github.com/syncthing/syncthing/releases/download/v${SYNCTHING_VERSION}/${tarball}"
| tar xvz \  
&& mv syncthing*/syncthing /usr/local/bin/syncthing \  
&& rm -rf syncthing*  
  
CMD ["syncthing"]  

