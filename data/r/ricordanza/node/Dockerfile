FROM ricordanza/develop  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
apt-get update -y && \  
apt-get install -y nodejs npm && \  
npm cache clean && \  
npm install n -g && \  
n stable && \  
ln -sf /usr/local/bin/node /usr/bin/node && \  
npm install -g browserify && \  
npm install -g gulp && \  
apt-get purge -y nodejs npm && \  
apt-get autoremove -y && \  
apt-get autoclean -y && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apt/* && \  
rm -rf /var/log/*  

