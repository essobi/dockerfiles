FROM node:9  
LABEL authors="Oleksandr Sochka, MaxymVlasov"  
  
# Set production settings  
ENV NODE_ENV=production \  
MONGODB_URL=mongodb://db:27017/dj-session \  
APP_HOST=open.wdc.org.ua \  
PRODUCTION=true \  
NPM_CONFIG_PRODUCTION=true  
  
RUN npm install -g sails grunt bower pm2 npm-check-updates  
  
WORKDIR /app  
  
COPY package.json package-lock.json ./  
RUN npm install  
  
COPY . /app  
  
# for some reason this is not called automatically in docker  
RUN npm run-script postinstall  
  
EXPOSE 80  
CMD ["sails", "lift"]  

