  
FROM node:0.10  
MAINTAINER Quiz Team  
  
  
WORKDIR /  
  
# Install Quiz Team Prerequisites  
RUN npm install -g gulp-cli  
RUN npm install -g bower  
  
# Install Quiz Team packages  
ADD package.json /package.json  
RUN npm install  
  
# Manually trigger bower. Why doesnt this work via npm install?  
ADD /client/.bowerrc /client/.bowerrc  
ADD /client/bower.json /client/bower.json  
WORKDIR /client  
RUN bower install --config.interactive=false \--allow-root  
WORKDIR ..  
  
# Make everything available for start  
ADD . /  
  
# Set development environment as default  
ENV NODE_ENV development  
  
# Port 3000 for server  
# Port 35729 for livereload  
EXPOSE 3000 35729  
CMD ["gulp"]

