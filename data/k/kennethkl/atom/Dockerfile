FROM ubuntu  
  
# Install atom dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
curl \  
ca-certificates \  
libgtk2.0-0 \  
libxtst6 \  
libnss3 \  
libgconf-2-4 \  
libasound2 \  
fakeroot \  
gconf2 \  
gconf-service \  
libcap2 \  
libnotify4 \  
libxtst6 \  
libnss3 \  
gvfs-bin \  
xdg-utils \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV ATOM_VERSION 1.0.19  
  
RUN curl -sSL
https://github.com/atom/atom/releases/download/v${ATOM_VERSION}/atom-amd64.deb
-o /tmp/atom-amd64.deb \  
&& dpkg -i /tmp/atom-amd64.deb \  
&& rm -rf /tmp/atom-amd64.deb  
  
CMD ["/usr/bin/atom","-f"]  

