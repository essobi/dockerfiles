FROM ubuntu:14.04  
  
RUN apt-get update \  
&& apt-get -y install curl libfontconfig \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN cd /tmp && curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
-o phantomjs.tar.bz2 \  
&& tar xjf phantomjs.tar.bz2 && mv /tmp/phantomjs-*/bin/phantomjs /usr/bin/ &&
rm -r /tmp/phantomjs*  
  
EXPOSE 8910  
  
CMD ["/usr/bin/phantomjs", "--wd"]  

