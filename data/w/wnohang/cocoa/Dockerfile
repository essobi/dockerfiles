# Generated automatically by update.sh  
# Do no edit this file  
FROM debian:8  
RUN apt-get update \  
&& apt-get install --yes wget libblas3gf  
  
RUN mkdir /opt/cocoa-5.2.2 \  
&& wget -O- http://cocoa.dima.unige.it/download/bin/cocoa-5.2.2-linux.tgz \  
| tar xzf - -C /opt/cocoa-5.2.2 --strip-components=1  
  
RUN apt-get remove --purge --yes wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /opt/cocoa-5.2.2/cocoa5 /usr/local/bin/cocoa  
  
CMD ["cocoa"]  

