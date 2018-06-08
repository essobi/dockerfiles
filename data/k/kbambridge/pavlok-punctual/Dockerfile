FROM node:7.10.0  
# Create app directory  
RUN useradd --user-group --create-home --shell /bin/false app  
  
ENV HOME=/home/app  
  
COPY package.json npm-shrinkwrap.json $HOME/pavlok/  
RUN chown -R app:app $HOME/*  
  
USER app  
WORKDIR $HOME/pavlok  
RUN npm install && npm cache clean  
  
USER root  
COPY . $HOME/pavlok  
RUN chown -R app:app $HOME/*  
USER app  
  
CMD [ "node", "app.js" ]  

