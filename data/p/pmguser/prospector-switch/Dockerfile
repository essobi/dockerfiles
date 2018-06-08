FROM node:9.5.0-stretch  
#FROM node:7.9.  
RUN groupadd -r application && useradd -r -g application application  
ENV HOME=/home/application  
WORKDIR $HOME/prospector-switch  
  
RUN /bin/su application \  
&& curl -sS http://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install -y yarn \  
&& mkdir $HOME/prospector-switch/logs \  
&& ln -f -s /usr/share/zoneinfo/America/Chicago /etc/localtime  
COPY package.json yarn.lock $HOME/prospector-switch/  
COPY . $HOME/prospector-switch  
RUN chown -R application:application $HOME/* && chown -R
application:application $HOME/* \  
&& yarn install  
  
EXPOSE 8002  
CMD ["node","./bin/server.js"]

