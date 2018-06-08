FROM node:alpine  
  
ADD . /src  
WORKDIR /src  
  
COPY package.json yarn.lock /src/  
  
RUN ["yarn"]  
RUN ["yarn", "cache", "clean"]  
RUN ["yarn", "build"]  
  
CMD ["yarn", "start"]  

