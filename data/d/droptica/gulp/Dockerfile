FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y build-essential nodejs nodejs-legacy npm rubygems ruby-
dev  
  
RUN gem update --system  
RUN gem install compass  
  
RUN npm install -g gulp-cli gulp-compass  
RUN npm link gulp  
  
CMD ["gulp", "watch"]  

