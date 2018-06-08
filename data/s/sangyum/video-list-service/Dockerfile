FROM mhart/alpine-node:8.1.3  
RUN addgroup -S app && adduser -S -g app app  
  
ENV HOME=/home/app  
  
WORKDIR $HOME  
COPY package.json $HOME/  
  
RUN npm install  
  
COPY index.js $HOME/index.js  
COPY youtube $HOME/youtube  
  
RUN chown -R app:app $HOME/*  
  
USER app  
CMD node ./index.js  

