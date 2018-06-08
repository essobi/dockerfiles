FROM node:9.5.0-stretch  
#FROM node:8.9.4-stretch  
RUN groupadd -r application && useradd -r -g application application  
ENV HOME=/home/application  
WORKDIR $HOME/prospector-redirect  
  
RUN /bin/su application \  
&& curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install -y yarn \  
&& mkdir $HOME/prospector-redirect/logs  
COPY package.json yarn.lock $HOME/prospector-redirect/  
COPY . $HOME/prospector-redirect  
RUN chown -R application:application $HOME/* && chown -R
application:application $HOME/* \  
&& yarn install  
  
EXPOSE 8003  
CMD ["node","./bin/server.js"]  

