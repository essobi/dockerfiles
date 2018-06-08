FROM node:6.1  
RUN groupadd -r application && useradd -r -g application application  
  
ENV HOME=/home/application  
  
COPY package.json $HOME/mc/  
RUN chown -R application:application $HOME/* && chown -R
application:application $HOME/*  
  
RUN /bin/su application  
WORKDIR $HOME/mc  
RUN npm i -g webpack gulp  
RUN npm install  
  
USER root  
COPY . $HOME/mc  
RUN chown -R application:application $HOME/*  
RUN BABEL_ENV=production webpack --config ./webpack/build-production.js  
RUN mkdir $HOME/mc/logs  
  
EXPOSE 80 27017 28015 29015  
CMD ["node","./bin/index.js"]  

