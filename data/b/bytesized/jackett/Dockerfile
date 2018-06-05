FROM bytesized/base  
MAINTAINER maran@bytesized-hosting.com  
  
ENV XDG_DATA_HOME="/config" \  
XDG_CONFIG_HOME="/config"  
  
RUN \  
apk add --no-cache \  
curl \  
libcurl \  
tar \  
wget && \  
apk add --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/main \  
python2 && \  
apk add --no-cache \  
\--repository http://nl.alpinelinux.org/alpine/edge/testing \  
mono && \  
  
mkdir -p \  
/app/Jackett && \  
jack_tag=$(curl -sX GET
"https://api.github.com/repos/Jackett/Jackett/releases/latest" \  
| awk '/tag_name/{print $4;exit}' FS='[""]') && \  
curl -o \  
/tmp/jacket.tar.gz -L \  
https://github.com/Jackett/Jackett/releases/download/$jack_tag/Jackett.Binaries.Mono.tar.gz
&& \  
tar xf \  
/tmp/jacket.tar.gz -C \  
/app/Jackett --strip-components=1 && \  
  
rm -rf \  
/tmp/*  
  
COPY static/ /  
  
VOLUME /config /data  
EXPOSE 9117  

