FROM node:wheezy  
  
RUN npm install castnow -g  
  
RUN echo deb http://www.deb-multimedia.org wheezy main >>
/etc/apt/sources.list  
  
RUN apt-get update  
RUN apt-get install -y --force-yes ffmpeg  
  
ENTRYPOINT ["/usr/local/bin/castnow"]  

