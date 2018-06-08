FROM mono  
  
RUN apt-get update && \  
apt-get install -y \  
mediainfo \  
wget && \  
rm -rf /var/lib/apt/lists/* && \  
curl -L https://git.io/vDYEI | grep -m1 -Po '(?<="browser_download_url":
")(.+\\.linux.tar.gz)' | xargs wget --quiet -O /tmp/Radarr.tar.gz && \  
tar -xvzf /tmp/Radarr.tar.gz -C /opt && \  
apt-get remove -y \  
wget && \  
apt-get autoremove -y && \  
apt-get clean -y  
  
EXPOSE 7878  
  
CMD ["mono", "/opt/Radarr/Radarr.exe", "-data=/mnt/config/radarr"]  

