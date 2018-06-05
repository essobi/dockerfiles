# -*- docker-image-name: "fiuba/autopdf" -*-  
  
FROM ubuntu:16.04  
  
# Dependencias.  
RUN apt-get update && apt-get upgrade -y && \  
env DEBIAN_FRONTEND=noninteractive apt-get install -y \  
jq \  
curl \  
gawk \  
git \  
make \  
pandoc \  
lmodern \  
cabextract \  
ca-certificates \  
texlive-xetex \  
texlive-lang-spanish \  
texlive-fonts-extra \  
texlive-fonts-recommended && \  
  
curl -Lo /tmp/ppv.exe \  
https://download.microsoft.com/download/E/6/7/E675FFFC-2A6D-4AB0-B3EB-27C9F8C8F696/PowerPointViewer.exe
&& \  
  
echo 'ab48a8ebac88219c84f293c6c1e81f1a0f420da6 /tmp/ppv.exe' \  
| sha1sum -c --status && \  
  
cabextract -s -F ppviewer.cab -d /tmp /tmp/ppv.exe && \  
  
cabextract -s -L -F 'CONSOLA*.TTF' \  
-d /usr/share/fonts/truetype/vista /tmp/ppviewer.cab && \  
  
fc-cache -f /usr/share/fonts/truetype/vista && rm -f /tmp/ppv*  
  
# TODO(dato): volver a añadir skicka.  
COPY ["bin/mk_autopdf", "/usr/local/bin/"]  

