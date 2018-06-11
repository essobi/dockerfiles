FROM dockerpro/cloud-lang-node  
  
RUN npm install -g bower grunt-cli  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
RUN npm install --production && \  
bower install --production --allow-root --config.interactive=false && \  
grunt build && \  
npm uninstall -g bower grunt-cli && \  
npm cache clear  
  
RUN echo "{\"gitHash\":\"$(git rev-parse --short HEAD)\"}" > dist/gitHash.json
&& \  
echo "{\"gitHash\":\"$(git rev-parse --short HEAD)\"}" > gitHash.json && \  
cat dist/gitHash.json && \  
rm -rf src && \  
rm -rf test && \  
rm -rf .tmp && \  
rm -rf .sass-cache  
  
EXPOSE 3000  
CMD ["npm", "start"]  

