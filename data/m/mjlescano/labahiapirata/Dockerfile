FROM node:slim  
  
MAINTAINER Matías Lescano <mjlescano@protonmail.com>  
  
COPY ["package.json", "/usr/src/"]  
  
WORKDIR /usr/src  
  
RUN npm install --quiet --production  
  
COPY [".", "/usr/src/"]  
  
ENV NODE_ENV=production \  
PORT=3000 \  
PIRATEBAY_HOST=https://thepiratebay.org \  
LOAD_ANALYTICS=false \  
ANALYTICS_CODE=UA-XXXXXXXX-X  
  
EXPOSE 3000  
CMD ["npm", "start"]  

