FROM barbudo/phantomjs  
  
USER app  
RUN mkdir ~/scripts  
WORKDIR /home/app/scripts  
  
ENV VERSION 0.0.3  
RUN curl -sSL https://github.com/ElbertF/Wappalyzer/archive/master.tar.gz |
tar xz \  
&& mkdir wappalyzer \  
&& cp Wappalyzer-master/src/drivers/phantomjs/driver.js ./wappalyzer \  
&& cp Wappalyzer-master/src/wappalyzer.js ./wappalyzer \  
&& cp Wappalyzer-master/src/apps.json ./wappalyzer \  
&& rm -rf ./Wappalyzer-master  
  
WORKDIR /home/app/scripts/wappalyzer  
  
ENTRYPOINT ["phantomjs", "--load-images=false", "--ignore-ssl-errors=true", "
--ssl-protocol=any", "./driver.js"]

