FROM mhart/alpine-node:latest  
LABEL maintainer="Tom Wagner <tomas.wagner@gmail.com>"  
  
# create workdir  
RUN mkdir -p /app  
  
# set workdir  
WORKDIR /app  
  
# install dependecies  
COPY package.json .  
COPY yarn.lock .  
RUN yarn install  
  
# copy app code  
COPY . .  
  
# entrypoint  
ENTRYPOINT yarn start  

