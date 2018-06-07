FROM jbogatay/baseimage-alpine-mono  
  
# install packages  
RUN \  
  
# install jackett  
mkdir -p /app/Jackett && \  
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
  
# cleanup  
rm -rf \  
/tmp/*  
  
# add local files  
COPY root/ /  
  
# ports and volumes  
VOLUME /config /downloads  
EXPOSE 9117  

