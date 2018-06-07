FROM node:0.12  
# Install gem sass for grunt-contrib-sass  
RUN apt-get update -qq && apt-get install -y build-essential  
RUN apt-get install -y ruby  
RUN gem install sass  
  
WORKDIR /home/fed  
  
# Install Mean.JS Prerequisites  
RUN npm install -g grunt-cli  
RUN npm install -g bower  
  
# Install Mean.JS packages  
ADD package.json /home/fed/package.json  
RUN npm install  
  
# Manually trigger bower. Why doesnt this work via npm install?  
ADD .bowerrc /home/fed/.bowerrc  
ADD bower.json /home/fed/bower.json  
RUN bower install --config.interactive=false \--allow-root  
  
# Make everything available for start  
ADD . /home/fed  
  
# Set development environment as default  
ENV NODE_ENV development  
  
# Port 3000 for server  
# Port 35729 for livereload  
EXPOSE 3000 35729  
CMD ["grunt", "prod"]  

