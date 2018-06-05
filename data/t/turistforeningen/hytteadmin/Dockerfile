FROM node:argon-slim  
  
RUN groupadd -r app && useradd -r -d /usr/src/app -g app app \  
&& apt-get -y --no-install-recommends update \  
&& apt-get -y --no-install-recommends install git \  
&& mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
CMD [ "/bin/true" ]  
  
COPY package.json /usr/src/app/  
RUN npm install  
  
COPY bower.json /usr/src/app/  
RUN npm run bower  
  
COPY . /usr/src/app  
  
RUN chown -R app:app /usr/src/app \  
&& runuser -l app -c 'npm run build' \  
&& apt-get -y autoclean \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

