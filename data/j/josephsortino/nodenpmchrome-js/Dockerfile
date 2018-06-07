FROM josephsortino/nodenpmchrome  
  
WORKDIR /usr/src/app  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists  
  
CMD npm test  
  
ONBUILD COPY package.json /usr/src/app/package.json  
ONBUILD RUN npm install  
ONBUILD COPY . /usr/src/app  

