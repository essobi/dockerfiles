# Template for Debian-based OSes  
FROM debian:jessie  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \  
ca-certificates \  
curl \  
&& curl -sLo /tmp/dumb-init.deb \  
https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-
init_1.0.2_amd64.deb \  
&& dpkg -i /tmp/dumb-init.deb \  
&& rm /tmp/dumb-init.deb \  
&& apt-get clean  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
  
# vim: ft=dockerfile  

