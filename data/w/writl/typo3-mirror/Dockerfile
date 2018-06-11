FROM ubuntu:wily  
  
RUN apt-get update && apt-get install -y \  
curl \  
wget \  
gnupg \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY load-all-typo3-src.sh /load-all-typo3-src.sh  
RUN chmod +x /load-all-typo3-src.sh && mkdir /data  
  
ENTRYPOINT ["/load-all-typo3-src.sh"]  

