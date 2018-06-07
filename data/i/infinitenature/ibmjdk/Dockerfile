FROM ibmjava:9-sdk  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
wget \  
\  
bzr \  
git \  
mercurial \  
openssh-client \  
subversion \  
\  
procps \  
  
&& rm -rf /var/lib/apt/lists/*  
  
RUN set -ex; \  
if ! command -v gpg > /dev/null; then \  
apt-get update; \  
apt-get install -y --no-install-recommends \  
gnupg \  
dirmngr \  
; \  
rm -rf /var/lib/apt/lists/*; \  
fi  

