FROM node:5.6.0-wheezy  
  
RUN apt-get update  
  
RUN npm install -g webpack coffee-script  
  
ADD . /src/  
  
WORKDIR /src/  
  
RUN cd dl/ && npm install  
RUN cd web/ && npm install  
  
RUN wget https://github.com/bitshares/bitshares-
js/releases/download/vBTS2_bloom_filter/bts_genesiskeys_bloom.dat -O
/src/web/app/assets/bts_genesiskeys_bloom.dat  
  
RUN cd web/ && npm run build  

