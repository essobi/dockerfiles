FROM node:5  
RUN mkdir /srv/kanban-client  
WORKDIR /srv/kanban-client  
  
COPY package.json /srv/package.json  
RUN npm config set registry http://registry.npmjs.org/  
RUN npm --prefix /srv --no-optional --quiet install && npm install -g webpack
&& npm install -g webpack-dev-server  
  
COPY . /srv/kanban-client  
WORKDIR /srv/kanban-client  
  
CMD ["npm start"]

