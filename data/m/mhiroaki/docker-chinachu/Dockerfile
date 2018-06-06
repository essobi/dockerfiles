FROM node:8-alpine as ffmpeg  
RUN apk add --no-cache openssl git python make gcc g++  
  
RUN wget -O /tmp/ffmpeg.tar.xz
https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-64bit-static.tar.xz \  
&& tar xJvf /tmp/ffmpeg.tar.xz \  
&& mv ffmpeg-*-64bit-static/ffmpeg /usr/local/bin/ \  
&& rm -rf /tmp/ffmpeg*  
  
FROM node:8-alpine as pm2  
RUN npm install -g pm2  
  
FROM node:8-alpine as chinachu  
RUN apk add --no-cache openssl git python make gcc g++  
WORKDIR /usr/src/app  
RUN git clone https://github.com/Chinachu/Chinachu.git .  
  
ENV NODE_ENV production  
  
RUN git submodule init  
RUN git submodule update  
RUN npm install  
RUN npm update  
  
RUN install -o node -g node config.sample.json config.json  
RUN install -o node -g node rules.sample.json rules.json  
RUN install -o node -g node -d log data recorded  
  
COPY processes.json .  
RUN rm -rf .git/  
RUN mv web/lib/ace/src-min-noconflict/ace.js . && rm -rf web/lib/ace && mkdir
-p web/lib/ace/src-min-noconflict/ && mv ace.js web/lib/ace/src-min-
noconflict/ace.js  
RUN mv web/lib/dc.js/dc.min.js . && rm -rf web/lib/dc.js && mkdir -p
web/lib/dc.js && mv dc.min.js web/lib/dc.js/dc.min.js  
RUN mv web/lib/d3/d3.min.js . && rm -rf web/lib/d3 && mkdir -p web/lib/d3 &&
mv d3.min.js web/lib/d3/d3.min.js  
RUN rm -rf web/lib/bootstrap/js  
RUN mv web/lib/crossfilter/crossfilter.min.js . && rm -rf web/lib/crossfilter/
&& mkdir -p web/lib/crossfilter/ && mv crossfilter.min.js
web/lib/crossfilter/crossfilter.min.js  
  
FROM node:8-alpine  
RUN apk add --no-cache bash  
COPY \--from=ffmpeg /usr/local/bin/ffmpeg /usr/local/bin/ffmpeg  
COPY \--from=pm2 /usr/local/lib/node_modules/pm2
/usr/local/lib/node_modules/pm2  
COPY \--from=chinachu /usr/src/app /usr/src/app  
COPY ./hacks/ /usr/local/bin/  
RUN chown node:node /usr/src/app/data /usr/src/app/recorded /usr/src/app/log \  
&& ln -s ../lib/node_modules/pm2/bin/pm2-runtime /usr/local/bin/ \  
&& ln -s ../lib/node_modules/pm2/bin/pm2 /usr/local/bin/  
  
WORKDIR /usr/src/app  
VOLUME /usr/src/app/data  
VOLUME /usr/src/app/recorded  
VOLUME /usr/src/app/log  
CMD ["pm2-runtime", "processes.json"]  
EXPOSE 20772  
USER node  

