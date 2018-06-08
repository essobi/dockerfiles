FROM ubuntu:latest  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \  
echo "deb http://download.mono-project.com/repo/debian wheezy main" | tee
/etc/apt/sources.list.d/mono-xamarin.list && \  
apt-get -y update && \  
apt-get -y install mono-devel mediainfo sqlite3 libmono-cil-dev curl
supervisor && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN useradd -m -s /bin/sh user && \  
passwd -d user  
  
RUN mkdir -p /opt && \  
cd /opt && \  
ver=$(curl -L https://api.github.com/repos/Radarr/Radarr/releases | grep -m1
tag_name | sed 's|.*"tag_name": "v\\([^"]\\+\\).*|\1|') && \  
curl -L -o radarr.tar.gz
"https://github.com/Radarr/Radarr/releases/download/v${ver}/Radarr.develop.${ver}.linux.tar.gz"
&& \  
tar xvf radarr.tar.gz && \  
rm radarr.tar.gz && \  
([ -d Radarr ] || mv [rR]adarr* Radarr) && \  
chmod -R +r Radarr  
  
EXPOSE 7878  
VOLUME /config /data  
  
ADD start.sh /  
ADD services.conf /etc/supervisor/conf.d/  
  
CMD ["/start.sh"]  

