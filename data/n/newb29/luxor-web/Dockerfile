# Define the image  
FROM node:7-alpine  
  
RUN apk add --no-cache make gcc g++ python bash git  
  
RUN npm install -g yarn  
  
ENV NODE_ENV production  
ENV APP_PATH /usr/src/app  
  
# Create the app directory  
RUN mkdir -p $APP_PATH  
  
WORKDIR $APP_PATH  
  
COPY . $APP_PATH  
  
RUN yarn install  
# RUN cd /tmp/app && \  
# yarn install && \  
# cp -a /tmp/app/. $APP_PATH  
# Bundle app source  
# COPY . $APP_PATH  
# COPY .env $APP_PATH  
# Run it in port 5433  
EXPOSE 5433  
# ENTRYPOINT ["sh", "./entrypoint.sh"]  
# Start it  
CMD [ "npm", "start" ]  

