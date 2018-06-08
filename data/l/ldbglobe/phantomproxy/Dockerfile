FROM debian:latest  
  
RUN apt-get update && apt-get install -y \  
npm \  
curl \  
bzip2 \  
libfreetype6 \  
libfontconfig  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install phantomjs  
COPY . /src  
RUN cd /src; npm install  
  
EXPOSE 8888  
CMD ["node", "/src/server.js"]

