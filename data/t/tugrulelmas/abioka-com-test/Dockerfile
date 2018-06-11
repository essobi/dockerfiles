FROM node:slim as nodeBuild  
  
RUN npm install gulp-cli -g  
COPY package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /opt/app && cp -a /tmp/node_modules /opt/app/  
WORKDIR /opt/app  
COPY . /opt/app  
RUN gulp  
RUN rm -rf dockerfile docker-compose.yml .gitignore gulpfile.js LICENSE
README.md node_modules less js/agency.js  
  
FROM nginx  
RUN rm -rf /usr/share/nginx/html/*  
COPY \--from=nodeBuild /opt/app /usr/share/nginx/html  

