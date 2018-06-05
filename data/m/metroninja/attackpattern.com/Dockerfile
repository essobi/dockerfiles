FROM node:6.5.0  
MAINTAINER Attack Pattern <hello@attackpattern.com>  
  
ENV SOURCE /src  
ENV NODE_PATH=$SOURCE  
ENV ASSETS_PATH=/public  
ENV APP_PORT=8080  
EXPOSE $APP_PORT  
  
RUN npm install -g webpack@4.1.1  
  
COPY ./package.json $SOURCE/package.json  
WORKDIR $SOURCE  
  
RUN npm install --slient  
ADD . $SOURCE  
RUN npm run prestart  
CMD npm start  

