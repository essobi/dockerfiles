FROM node:0.10  
MAINTAINER Stepan Kuzmin <to.stepan.kuzmin@gmail.com>  
  
ENV VERSION 0.3.8  
RUN mkdir -p /usr/src/mapbox-studio-classic \  
&& curl -SLO "https://github.com/mapbox/mapbox-studio-
classic/archive/v$VERSION.tar.gz" \  
&& tar xzf "v$VERSION.tar.gz" \--strip-components 1 -C /usr/src/mapbox-studio-
classic \  
&& rm "v$VERSION.tar.gz" \  
&& cd /usr/src/mapbox-studio-classic \  
&& npm install  
  
WORKDIR /usr/src/mapbox-studio-classic  
VOLUME /root  
EXPOSE 3000  
CMD [ "npm", "start" ]  

