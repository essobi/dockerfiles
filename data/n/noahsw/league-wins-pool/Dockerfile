FROM node:0.12.2  
  
# Install dependencies  
RUN apt-get update -y  
RUN apt-get install ruby-full -y  
RUN gem install compass -v 1.0.3  
  
# Install PhantomJS dependencies (https://github.com/karma-runner/karma-
phantomjs-launcher/issues/31)  
RUN apt-get install build-essential chrpath libssl-dev libxft-dev -y  
RUN apt-get install libfreetype6 libfreetype6-dev -y  
RUN apt-get install libfontconfig libfontconfig1 libfontconfig1-dev -y  
  
# Build client-side app within the container so we don't have to include it in
our repo  
WORKDIR /app  
RUN npm install -g grunt-cli@0.1.13  
RUN npm install -g bower@1.3.8  
RUN npm install -g phantomjs@1.9.7-14  
RUN npm install -g nodemon@1.3.7  
  
ADD . /app  
WORKDIR /app/client  
RUN bower install --allow-root # --allow-root allows bower to run as sudo,
which is how Docker runs it  
RUN npm install  
RUN grunt --force  
  
WORKDIR /app/server  
RUN npm install  
  
EXPOSE 3000  
  
CMD npm start  

