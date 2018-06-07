FROM node:7  
MAINTAINER Jérôme Quéré <contact@jeromequere.com>  
WORKDIR /mnt/app  
EXPOSE 8080  
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.2.0/dumb-init_1.2.0_amd64  
RUN chmod +x /usr/local/bin/dumb-init  
ENTRYPOINT ["/usr/local/bin/dumb-init"]  
CMD ["./node_modules/.bin/coffee", "index.coffee"]  
COPY package.json /mnt/app  
RUN npm install --production  
COPY . /mnt/app  

