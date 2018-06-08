FROM docker.io/node:6  
RUN npm install -g mocha istanbul nodemon gulp bower mocha-bamboo-reporter
tick  
  
WORKDIR /srv/app  
  
CMD [ "node", "src/index.js", "--max_old_space_size=250" ]  
  

