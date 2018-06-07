FROM ricordanza/aws  
  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh && \  
apt-get update -y && \  
pip install lambda-uploader python-lambda-local lamvery && \  
curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh && \  
apt-get autoremove && \  
apt-get autoclean && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apt/* && \  
rm -rf /var/log/*  

