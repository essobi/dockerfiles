FROM nginx:alpine  
LABEL maintainer Nathan Douglas <docker@tenesm.us>  
RUN apk add \--no-cache --virtual parchment-dependencies git &&\  
git clone https://github.com/curiousdannii/parchment.git /parchment &&\  
cd /parchment &&\  
git submodule update \--init --recursive &&\  
mkdir -p /parchment/index &&\  
mv /parchment/index.html /parchment/index/index.html &&\  
ln -sf /parchment/index/index.html /parchment/index.html &&\  
rm -rf /usr/share/nginx/html &&\  
ln -sf /parchment /usr/share/nginx/html &&\  
apk del parchment-dependencies  
VOLUME /parchment/index  
VOLUME /parchment/stories  

