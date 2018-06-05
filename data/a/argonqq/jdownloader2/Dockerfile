FROM java  
MAINTAINER Marcel Sinn <loopyargon@gmail.com>  
  
RUN \  
apt-get update &&\  
apt-get -y install\  
ffmpeg &&\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD http://installer.jdownloader.org/JD2SilentSetup_x64.sh
/tmp/JD2SilentSetup_x64.sh  
RUN \  
adduser --disabled-password --quiet --gecos '' jdownloader &&\  
mkdir -p /download\ &&\  
chown jdownloader /tmp/JD2SilentSetup_x64.sh &&\  
chmod +x /tmp/JD2SilentSetup_x64.sh &&\  
sleep 1 &&\  
echo -e "\n\n\n"|/tmp/JD2SilentSetup_x64.sh; \  
chown -R jdownloader:jdownloader /usr/local/jd2 /download\ &&\  
echo '{ "defaultdownloadfolder" : "/download" }'
>/usr/local/jd2/cfg/org.jdownloader.settings.GeneralSettings.json  
  
USER jdownloader  
VOLUME /download  
CMD ["/usr/local/jd2/JDownloader2"]  

