FROM node:5-slim  
  
RUN (echo "deb http://opensource.nchc.org.tw/debian jessie main" >
/etc/apt/sources.list) && \  
(echo "deb http://opensource.nchc.org.tw/debian jessie-updates main" >>
/etc/apt/sources.list) && \  
(echo "deb http://opensource.nchc.org.tw/debian jessie-backports main" >>
/etc/apt/sources.list) && \  
(echo "deb http://security.debian.org jessie/updates main" >>
/etc/apt/sources.list) && \  
apt-get update && \  
apt-get install -y imagemagick unzip --no-install-recommends && \  
apt-get -t jessie-backports install -y ffmpeg --no-install-recommends && \  
rm -rf /var/lib/apt/lists/* && \  
curl -OJL
https://github.com/pornel/giflossy/releases/download/lossy%2F1.82.1/gifsicle-1.82.1-lossy.zip
&& \  
unzip gifsicle-1.82.1-lossy.zip -d gifsicle && \  
rm -f gifsicle-1.82.1-lossy.zip && \  
cp gifsicle/linux/gifsicle-debian6 /usr/bin/gifsicle && \  
rm -rf gifsicle && \  
npm install -g gifify && \  
rm -rf ~/.npm  
  
CMD ["gifify"]  

