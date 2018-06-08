FROM keymetrics/pm2-docker-alpine:6  
ENV PORT=3000  
EXPOSE $PORT  
  
RUN mkdir -p /usr/src/ico-scrapper  
  
WORKDIR /usr/src/ico-scrapper  
  
COPY package.json npm-shrinkwrap.json ./  
  
COPY pm2.json .  
  
RUN npm install --production --silent --progress=false  
  
RUN npm install --silent --progress=false && npm cache clean --force  
  
COPY ./*.js ./  
  
CMD ["pm2-docker", "pm2.json"]

