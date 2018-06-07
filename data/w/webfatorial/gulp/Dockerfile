FROM node:slim  
  
MAINTAINER webfatorial <webfatorial@webfatorial.com>  
  
RUN npm install -g gulp  
  
RUN apt-get update  
RUN apt-get -y install libxml2-dev  
RUN apt-get -y install libxslt1-dev  
RUN apt-get -y install libreadline6-dev  
RUN apt-get -y install build-essential  
RUN apt-get -y install ruby  
RUN apt-get -y install ruby-ffi  
RUN apt-get -y install zlib1g-dev  
  
RUN gem update --system  
RUN gem install --no-rdoc --no-ri sass  
RUN gem install --no-rdoc --no-ri compass  
RUN gem install --no-rdoc --no-ri sass-css-importer --pre  
RUN gem install --no-rdoc --no-ri breakpoint  
  
EXPOSE 35729  

