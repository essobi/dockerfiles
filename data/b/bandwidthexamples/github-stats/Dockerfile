FROM node:8-alpine  
WORKDIR /src  
ADD . /src  
ADD https://github.com/pugnascotia/mantra/releases/download/0.0.1/mantra
/usr/bin  
RUN npm install --global yarn && \  
yarn install && \  
chmod +x /usr/bin/mantra && \  
yarn run build && \  
rm -rf node_modules && \  
rm -rf assets/node_modules && \  
gzip -9 $(find assets/dist -type f \\( -name "*.js" -or -name "*.css" \\)) &&
\  
yarn install --prod && \  
yarn cache clean  
EXPOSE 3000  
ENTRYPOINT sh ./tools/docker-start.sh  

