# Dockerfile  
# spotify-client  
  
FROM debian:jessie  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \  
\--recv-keys 0DF731E45CE24F27EEEB1450EFDC8610341D9410 >/dev/null && \  
echo deb http://repository.spotify.com stable non-free > \  
/etc/apt/sources.list.d/spotify.list && \  
apt-get -qq update && \  
apt-get -qqy install spotify-client  

