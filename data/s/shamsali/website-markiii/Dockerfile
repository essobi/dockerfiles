FROM node:6-wheezy  
  
RUN mkdir -p /app  
WORKDIR /app  
COPY package.json /app/  
COPY . /app  
  
# Install Git For Bower  
RUN apt-get -q update && apt-get install -y -qq \  
git \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install  
  
# Install Bower  
RUN npm install --quiet -g bower \  
&& npm cache clean  
  
# Install ruby-sass  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends ruby-sass \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean -y \  
&& apt-get autoremove -y  
  
COPY bower.json /app/  
RUN bower install --allow-root  
RUN npm install -g grunt  
RUN cd /app  
EXPOSE 9000 80 443 27017 8080  
CMD npm start

