FROM node:argon  
  
# Bundle app source  
COPY . app/  
WORKDIR app/  
  
# Install gem Sass  
RUN apt-get update \  
&& apt-get install -y ruby \  
&& gem install sass -v 3.2.19  
  
# Install app dependencies  
RUN npm install \  
&& npm install -g grunt bower \  
&& echo '{ "allow_root": true }' > .bowerrc \  
&& bower install  
  
# Build production version of the website  
RUN grunt build --trace  
  
EXPOSE 9000  
CMD [ "node", "dist/server/app.js" ]  

