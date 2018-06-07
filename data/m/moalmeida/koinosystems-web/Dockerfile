FROM moalmeida/docker-nodejs:latest  
MAINTAINER "moalmeida" <moalmeida@koinosystems.com>  
  
ADD app $HOME  
RUN npm-cache install --cacheDirectory /app/.npm_cache npm  
  
CMD ["npm", "start"]  

