FROM debian:jessie-slim  
  
RUN groupadd --gid 1000 pandoc \  
&& useradd --uid 1000 --gid pandoc --shell /bin/bash --create-home pandoc  
  
RUN set -ex \  
\  
&& buildDeps=' \  
ca-certificates \  
wget \  
' \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $buildDeps \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget
"https://github.com/jgm/pandoc/releases/download/1.15.2/pandoc-1.15.2-1-amd64.deb"
\  
&& dpkg -i pandoc-1.15.2-1-amd64.deb \  
&& rm pandoc-1.15.2-1-amd64.deb  
  
RUN apt-get purge -y --auto-remove $buildDeps  
  
CMD [ "bash" ]  

