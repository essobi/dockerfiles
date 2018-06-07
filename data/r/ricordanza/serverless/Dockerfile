FROM ricordanza/node  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
apt-get update -y && \  
apt-get install -y python-pip && \  
pip install awscli && \  
npm install -g serverless && \  
apt-get autoremove && \  
apt-get autoclean && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apt/* && \  
rm -rf /var/log/*  

