FROM mono  
  
COPY init-config.sh /tmp/init-config.sh  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
sqlite3 \  
unzip \  
wget && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sL http://git.io/viA9C | grep -Po '(?<="browser_download_url":
")(.+\.zip)' | xargs wget --quiet -O /tmp/Ombi.zip && \  
unzip /tmp/Ombi.zip -d /tmp && \  
mkdir -p /opt/ombi && \  
mv /tmp/Release/* -t /opt/ombi && \  
chmod +x /tmp/init-config.sh; sync && \  
/tmp/init-config.sh && \  
apt-get remove -y \  
curl \  
unzip \  
wget && \  
apt-get autoremove -y && \  
apt-get clean -y  
  
EXPOSE 3579  
  
CMD ["mono", "/opt/ombi/Ombi.exe"]  

