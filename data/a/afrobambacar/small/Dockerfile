# ref. http://jdlm.info/articles/2016/03/06/lessons-building-node-app-
docker.html  
FROM node:6.11.2  
RUN useradd --user-group --create-home --shell /bin/false app  
  
ENV HOME=/home/app  
  
COPY package.json npm-shrinkwrap.json $HOME/app/  
RUN chown -R app:app $HOME/*  
  
USER app  
WORKDIR $HOME/app  
RUN npm install \  
&& npm cache clean  
  
USER root  
COPY . $HOME/app  
RUN chown -R app:app $HOME/*  
USER app  
  
CMD ["node", "index.js"]

