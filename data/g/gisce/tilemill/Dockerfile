FROM ubuntu:14.04  
MAINTAINER Gisce "devel@gisce.net"  
RUN apt-get update  
RUN apt-get -y upgrade  
  
RUN apt-get -y install nodejs-legacy npm git  
  
RUN git clone https://github.com/mapbox/tilemill.git  
RUN sed -i 's/"carto": ".*$/"carto":
"https\:\/\/github.com\/gisce\/carto\/archive\/extends_zoom_level.tar.gz",/g'
tilemill/package.json  
#RUN cat tilemill/package.json | sed 's/"carto": ".*$/"carto":
"https\:\/\/github.com\/gisce\/carto\/archive\/extends_zoom_level.tar.gz",/g'
>tilemill/tmp.json  
#RUN rm tilemill/package.json  
#RUN mv tilemill/tmp.json tilemill/package.json  
RUN npm install /tilemill/  
  
RUN sed -i "s/.*'maximum': 22,/\'maximum\': 25,/g"
/node_modules/tilemill/models/Project.bones  
RUN echo '{"server":true,"listenHost": "0.0.0.0"}' > /etc/tilemillconfig.json  
CMD /node_modules/tilemill/index.js start --config=/etc/tilemillconfig.json  
EXPOSE 20009  
EXPOSE 20008  

