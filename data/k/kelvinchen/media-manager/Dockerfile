FROM kelvinchen/torrent-utils:latest  
  
RUN \  
# Install latest version of Sonarr (also install Radarr dependencies)  
apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys FDA5DFFC \  
&& echo "deb http://apt.sonarr.tv/ master main" >
/etc/apt/sources.list.d/sonarr.list \  
&& apt-get update \  
&& apt-get install -y \--no-install-recommends nzbdrone libcurl4-openssl-dev
mono-devel \  
&& rm -rf /var/lib/apt/lists/* \  
# Install latest Radarr  
&& curl -sL $(curl -sL https://api.github.com/repos/Radarr/Radarr/releases |
grep browser_download_url | grep linux | head -n 1 | cut -d '"' -f 4) \  
| tar xz -C /opt \  
# Install latest Jackett  
&& curl -sL $(curl -sL https://api.github.com/repos/Jackett/Jackett/releases |
grep browser_download_url | grep Mono | head -n 1 | cut -d '"' -f 4) \  
| tar xz -C /opt  
  
# Set Jackett config path  
ENV XDG_DATA_HOME="/config" \  
XDG_CONFIG_HOME="/config"  
  
VOLUME /config  
  
EXPOSE 8989 7878 9117  
  
COPY services.d /etc/services.d  
  
CMD ["/init"]  

