FROM debian:stretch-slim  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
curl git ca-certificates gnupg dirmngr \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -sL "https://github.com/just-
containers/s6-overlay/releases/download/v1.21.2.2/s6-overlay-amd64.tar.gz" \  
| tar xz -C /  

