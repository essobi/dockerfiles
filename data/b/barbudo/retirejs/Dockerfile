FROM barbudo/phantomjs  
  
USER app  
RUN mkdir ~/scripts  
WORKDIR /home/app/scripts  
  
ENV VERSION 0.0.2  
RUN curl -sSL https://github.com/m0sth8/retire.js/archive/master.tar.gz | tar
xz \  
&& mv ./retire.js-master ./retirejs  
  
WORKDIR /home/app/scripts/retirejs/phantomjs/  
  
ENTRYPOINT ["phantomjs", "--load-images=false", "--ignore-ssl-errors=true", "
--ssl-protocol=any", "./scan.js"]

