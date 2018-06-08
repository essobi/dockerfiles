FROM node:7-slim  
  
LABEL name="mugtalk"  
  
MAINTAINER Matías Lescano <mjlescano@protonmail.com>  
  
RUN npm set progress=false && npm install -g yarn  
  
COPY ["package.json", "yarn.lock", ".yarnclean", "/usr/src/"]  
  
WORKDIR /usr/src  
  
RUN yarn --production  
  
COPY [".", "/usr/src/"]  
  
ENV NODE_ENV=production  
  
RUN yarn build  
  
EXPOSE 3000  
CMD ["yarn", "start"]  

