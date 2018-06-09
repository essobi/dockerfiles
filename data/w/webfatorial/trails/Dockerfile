FROM node  
  
MAINTAINER webfatorial <webfatorial@webfatorial.com>  
  
RUN apt-get update  
RUN apt-get -y install git  
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
  
RUN npm install -g gulp  
RUN npm install -g bower  
RUN npm install -g yo  
RUN npm install -g generator-trails  
  
RUN useradd -ms /bin/bash docker  
  
USER docker  
  
EXPOSE 35729  

