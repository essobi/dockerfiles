FROM nginx  
MAINTAINER Kevin Traver  
  
RUN apt-get update -yq && apt-get upgrade -yq  
RUN apt-get -y install curl  
RUN apt-get -y install gnupg2  
RUN apt-get -y install git-core  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
RUN npm install -g ember-cli bower  
  
RUN mkdir -p /usr/src  
WORKDIR /usr/src  
  
ADD nginx.conf nginx.conf  
  
ADD ember-cli-build.js ember-cli-build.js  
ADD bower.json bower.json  
ADD package.json package.json  
  
ADD app app  
ADD config config  
  
RUN npm install  
RUN bower install --allow-root  
RUN ember build --environment=production --output-path=/usr/share/nginx/html  
  
RUN rm -rf bower_components  
RUN rm -rf node_modules  
  
COPY nginx.conf /etc/nginx/nginx.conf  

