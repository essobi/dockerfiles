FROM debian:jessie  
  
RUN apt-get update \  
&& runtimeDeps=" \  
wget \  
curl \  
varnish \  
" \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -qq -y --no-install-
recommends $runtimeDeps  
  
EXPOSE 80  
  

