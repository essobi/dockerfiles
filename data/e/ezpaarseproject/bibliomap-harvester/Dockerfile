FROM node:6.9.1  
# install yarn (faster than npm...)  
RUN npm config set strict-ssl false  
RUN apt-get update && apt-get install -y apt-transport-https  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update && apt-get install -y yarn  
  
# install parallel dependencie  
RUN apt-get install -y parallel  
  
# install npm dependencies  
WORKDIR /app  
COPY ./package.json /app/package.json  
RUN yarn install && yarn cache clean  
  
# copy the code source  
# after dependencies installation  
COPY . /app  
RUN mkdir -p /app/tmp  
  
# ezmasterification  
# see https://github.com/Inist-CNRS/ezmaster  
# (no data directory)  
# http port is not used  
RUN echo '{ \  
"httpPort": 3000, \  
"configPath": "/app/config.json" \  
}' > /etc/ezmaster.json  
  
# run the application  
ENTRYPOINT [ "./docker-entrypoint.njs" ]

