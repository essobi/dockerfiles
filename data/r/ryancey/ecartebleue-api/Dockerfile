FROM vitr/casperjs  
  
WORKDIR /home/ecb-api  
  
RUN apt-get update  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y build-essential nodejs  
  
RUN npm init -f -y  
RUN npm install express body-parser shell-escape forever  
  
ENV NODE_PATH /home/ecb-api/node_modules  
  
EXPOSE 3000  
COPY ./generate.js .  
COPY ./serve.js .  
  
ENTRYPOINT ["./node_modules/.bin/forever", "--watch", "serve.js"]

