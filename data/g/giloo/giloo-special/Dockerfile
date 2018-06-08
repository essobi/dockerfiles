FROM node:8.9.1  
MAINTAINER Chuck Yang <chuck@giloo.ist>  
  
ENV NODE_ENV=production  
ENV HOST 0.0.0.0  
# Create app directory  
RUN mkdir -p /app  
WORKDIR /app  
  
# Bundle app source  
COPY . /app  
# COPY package.json ./  
# COPY node_modules ./node_modules/  
# COPY dist ./dist  
RUN npm install pm2 -g  
  
# Expose the app port  
EXPOSE 3000  
# RUN npm cache clean --force && npm cache verify  
RUN npm install  
# RUN npm run build  
CMD [ "pm2", "start", "ecosystem.json" ]  

