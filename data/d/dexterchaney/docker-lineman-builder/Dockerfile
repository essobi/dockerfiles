FROM node:6  
RUN apt-get update && \  
apt-get install -y build-essential chrpath libssl-dev libxft-dev libfreetype6
libfreetype6-dev libfontconfig1 libfontconfig1-dev && \  
rm -fr /var/lib/apt/lists/*  
RUN npm install -g lineman bower  
ADD install-phantomjs.sh /  
RUN sh /install-phantomjs.sh  
RUN npm install -g testem  

