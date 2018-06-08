FROM node:8.2.0  
  
ARG PORT=8080  
ENV PORT $PORT  
ARG NODE_ENV=production  
ENV NODE_ENV $NODE_ENV  
ARG DATABASE_NAME=production  
ENV DATABASE_NAME $DATABASE_NAME  
ARG DATABASE_URL=postgres://predictev:predictev@connect.ccvzrv8yzkmn.us-
west-1.rds.amazonaws.com:5432/sc2  
ENV DATABASE_URL $DATABASE_URL  
ARG STEEMJS_URL=https://api.predictev.com:8443  
ENV STEEMJS_URL $STEEMJS_URL  
ARG STEEMJS_URL_LOCAL=http://jussi:8080  
ENV STEEMJS_URL_LOCAL $STEEMJS_URL_LOCAL  
ARG BROADCASTER_USERNAME=connect  
ENV BROADCASTER_USERNAME $BROADCASTER_USERNAME  
RUN npm install -g yarn sequelize-cli  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN yarn && yarn build  
  
EXPOSE $PORT  
RUN chmod +x /usr/src/app/bin/www  
CMD ["yarn", "start"]  

