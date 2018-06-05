FROM node:0.12.7  
MAINTAINER Oleg Ozimok "ozimok.oleg@gmail.com", Andrey Torba
andrey.torba@gmail.com  
  
RUN npm install -g bower gulp  
  
RUN mkdir -p /broomy/web  
  
WORKDIR /broomy/web  
  
COPY package.json /broomy/web/package.json  
RUN npm install  
  
COPY bower.json /broomy/web/bower.json  
RUN bower --allow-root install  
  
COPY . /broomy/web  
  
RUN gulp test \  
&& gulp build  
  
VOLUME /broomy/web  
  
# CMD ["gulp", "serve:dist"]  

