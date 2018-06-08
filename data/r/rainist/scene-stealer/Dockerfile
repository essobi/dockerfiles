FROM alekzonder/puppeteer:1.0.0  
  
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global  
ENV PATH=$PATH:/home/node/.npm-global/bin  
ENV NODE_ENV=production  
  
USER node  
  
RUN mkdir -p /home/node/app  
WORKDIR /home/node/app  
  
RUN npm i -g scene-stealer@1.0.9  
  
CMD ["scene-stealer"]  

