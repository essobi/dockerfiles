FROM binded/node-ci:base  
  
# Install Graphicsmagick from sid (package in jessie has bugs with PSD files)  
  
RUN echo "deb-src http://httpredir.debian.org/debian/ sid main contrib non-
free" \  
>> /etc/apt/sources.list.d/sources.list \  
&& echo "deb http://ftp.debian.org/debian jessie-backports main" \  
>> /etc/apt/sources.list.d/sources.list \  
&& cat /etc/apt/sources.list.d/sources.list \  
&& apt-get update \  
&& apt-get install -y build-essential \  
&& mkdir -p /tmp/gm-build \  
&& cd /tmp/gm-build \  
&& apt-get build-dep -y graphicsmagick \  
&& apt-get -b source graphicsmagick \  
&& dpkg -i libgraphicsmagick-q16-3_1.3.25-*_amd64.deb \  
&& dpkg -i graphicsmagick_1.3.25-*_amd64.deb \  
&& rm -rf /tmp/gm-build \  
&& rm -rf /var/lib/apt/lists/*  

