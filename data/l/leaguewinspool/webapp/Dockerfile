FROM leaguewinspool/webapp-base:3  
# Install node packages  
COPY package.json /webapp/  
COPY npm-shrinkwrap.json /webapp/  
WORKDIR /webapp  
RUN npm install  
  
# Install bower packages  
COPY assets/bower.json /webapp/assets/  
WORKDIR /webapp/assets  
RUN bower install  
  
# Add app files to container  
# Everything above this line should be cached in most cases  
COPY . /webapp  
  
# Sails.js requires active user to write to layout.ejs
(https://www.npmjs.com/package/grunt-sails-linker)  
# It'd be ideal if the COPY command above automatically gave write access to
the node user but I'm not sure why that isn't happening.  
# So we'll just force it here:  
USER root  
RUN chown -R node:node /webapp/views/layout.ejs  
USER node  
  
EXPOSE 3000  
WORKDIR /webapp  
  
CMD ["npm", "start"]  

