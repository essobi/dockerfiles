FROM node:7.5.0  
MAINTAINER phonoloop <phonoloop@spaceape.be>  
  
# Install general requirements  
RUN apt-get update -qq \  
&& apt-get install -y build-essential  
  
# Define volume  
VOLUME ./www/app  
# Define working directory  
WORKDIR /var/www/app  
  
# Install SASS  
RUN apt-get install -y ruby  
RUN gem install sass  
  
# Install Gulp 4.0 (alpha) and Bower globally  
RUN npm install gulpjs/gulp-cli -g  
RUN npm install -g bower  
  
# Include JSON files  
ADD ./www/app/package.json /var/www/app/package.json  
ADD ./www/app/bower.json /var/www/app/bower.json  
  
# Install dependencies from JSON files  
RUN echo '{ "allow_root": true }' > /root/.bowerrc \  
&& bower install \  
&& npm install --save-dev  
  
# Start default gulp  
CMD ["gulp"]

