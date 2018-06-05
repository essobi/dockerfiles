FROM node:latest  
LABEL version="0.1.01"  
MAINTAINER Marc Perrin-Pelletier <marc.perrinpelletier@gmail.com>  
  
WORKDIR /var/www/stbk  
  
RUN useradd -ms /bin/bash stbk  
  
RUN chown -R stbk:stbk /var/www  
USER stbk  
  
COPY package.json ./  
RUN npm install  
  
COPY bower.json \  
gulpfile.js \  
./  
COPY client client/  
COPY devops/build devops/build/  
RUN ./node_modules/bower/bin/bower install && ./node_modules/.bin/gulp build  
  
COPY api api/  
COPY config config/  
COPY app.coffee \  
.sailsrc \  
README.md \  
./  
  
VOLUME /var/www/stbk/web  
  
CMD ./node_modules/.bin/coffee app.coffee  

