FROM node:6.9.4  
# install yarn (faster than npm...)  
RUN npm config set strict-ssl false  
RUN apt-get update && apt-get install -y apt-transport-https  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -y yarn  
  
# install npm dependencies  
WORKDIR /app  
COPY ./package.json /app/package.json  
RUN yarn install && yarn cache clean  
  
# add source after install, for cache optimization  
COPY . /app  
  
# for ezMASTER  
# see https://github.com/Inist-CNRS/ezmaster  
RUN echo '{ \  
"httpPort": 27779, \  
"configPath": "/app/config.json" \  
}' > /etc/ezmaster.json  
  
EXPOSE 27779  
CMD ["npm", "start"]  

