  
FROM node:5.11  
MAINTAINER phyng  
  
RUN mkdir -p /app/src  
WORKDIR /app/src  
COPY package.json /app/src/  
RUN npm install --registry=http://registry.npm.taobao.org -g gulp gulp-coffee
coffee-script  
RUN PHANTOMJS_CDNURL=https://npm.taobao.org/dist/phantomjs npm install phantom
--registry=https://registry.npm.taobao.org --no-proxy  
RUN npm install --registry=http://registry.npm.taobao.org  
  
# NotoSansCJK  
RUN apt-get update && apt-get install unzip  
RUN mkdir -p /usr/share/fonts/truetype/noto/  
RUN curl https://noto-
website-2.storage.googleapis.com/pkgs/NotoSansCJK.ttc.zip -o
/usr/share/fonts/truetype/noto/NotoSansCJK.ttc.zip  
RUN unzip /usr/share/fonts/truetype/noto/NotoSansCJK.ttc.zip -d
/usr/share/fonts/truetype/noto/  
RUN rm /usr/share/fonts/truetype/noto/NotoSansCJK.ttc.zip  
RUN fc-cache -f -v  
  
COPY ./ /app/src/  
RUN gulp build  
  
ENV ENV_SERVER_PORT 7001  
EXPOSE 7001  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.0.3/dumb-init_1.0.3_amd64  
RUN chmod +x /usr/local/bin/dumb-init  
  
CMD ["dumb-init", "node", "app.js"]  

