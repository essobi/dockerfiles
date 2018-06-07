FROM mhart/alpine-node:8  
EXPOSE 80  
RUN apk update && \  
apk upgrade && \  
apk add --no-cache bash  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# install dependencies  
COPY package.json /usr/src/app/  
  
RUN npm install --quiet  
  
# install project  
COPY . /usr/src/app  
  
CMD node .  

