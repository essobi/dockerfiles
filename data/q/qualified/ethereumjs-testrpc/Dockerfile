FROM node:8.7.0-alpine  
  
ENV NPM_CONFIG_LOGLEVEL=warn NODE_ENV=production  
RUN npm install -g ethereumjs-testrpc@4.1.3  
  
EXPOSE 8545  
USER nobody  
ENTRYPOINT ["testrpc"]  

