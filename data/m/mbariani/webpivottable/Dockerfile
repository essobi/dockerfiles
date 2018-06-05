FROM ubuntu:15.10  
MAINTAINER "Michele Bariani" <michele.bariani@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y \  
npm \  
curl \  
bzip2 \  
unzip \  
&& \  
curl -sL https://deb.nodesource.com/setup_4.x | bash - && \  
apt-get install -y nodejs && \  
useradd -m wpt && \  
cd /home/wpt && \  
curl -O -J -L http://webpivottable.com/downloads/1302 && \  
unzip *.zip -d . && \  
npm install && \  
rm *.zip && \  
apt-get purge -y \  
npm \  
curl \  
bzip2 \  
unzip \  
&& \  
apt-get autoremove -y && \  
apt-get clean all  
  
USER wpt  
WORKDIR /home/wpt  
ENTRYPOINT ["node", "app"]  
EXPOSE 8002  

