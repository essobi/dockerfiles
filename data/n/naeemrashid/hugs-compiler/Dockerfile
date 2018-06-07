FROM debian:jessie-slim  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get update && apt-get install -y \  
libhugs-base-bundled \  
libhugs-haskell98-bundled \  
hugs \  
haskell-doc \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
ENV http_proxy=""  
ENV https_proxy=""  
ENTRYPOINT [ "hugs" ]  
  

