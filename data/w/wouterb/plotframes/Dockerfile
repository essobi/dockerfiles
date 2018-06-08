FROM ubuntu:16.04  
  
RUN apt-get update -y \  
&& apt-get install -y \  
ffmpeg \  
gnuplot \  
npm \  
nodejs \  
&& npm install plotframes -g \  
&& ln -s /usr/bin/nodejs /usr/bin/node \  
&& npm cache clear \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /usr/share/doc/ \  
&& rm -rf /usr/share/man/ \  
&& rm -rf /usr/share/locale/  
  
ENTRYPOINT [ "plotframes" ]  

