FROM debian:jessie  
  
RUN apt-get update -y && apt-get install -y --no-install-recommends \  
syslinux-utils \  
curl \  
ca-certificates \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sSL https://www.browserstack.com/browserstack-
local/BrowserStackLocal-linux-x64.zip \  
> /tmp/browserstack.zip && \  
unzip /tmp/browserstack.zip -d /tmp && \  
mv /tmp/BrowserStackLocal /usr/bin/browserstack  
  
RUN apt-get remove -y \  
syslinux-utils \  
curl \  
ca-certificates \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["browserstack"]  
CMD ["-h"]  

