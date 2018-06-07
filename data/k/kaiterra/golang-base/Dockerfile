FROM debian:jessie-slim  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
dnsutils \  
curl \  
netcat-openbsd \  
iputils-ping \  
texlive \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY zoneinfo.zip /usr/local/go/lib/time/  

