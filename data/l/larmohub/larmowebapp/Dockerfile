FROM debian:jessie  
MAINTAINER Marcin Wójcik <mwojcik@future-processing.com>, Mateusz Książek
<mksiazek@future-processing.com>  
  
RUN apt-get update && \  
apt-get -yq --no-install-recommends install \  
nodejs-legacy \  
npm \  
ruby \  
git \  
&& apt-get purge -y --auto-remove \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV API_URL http://0.0.0.0:5100  
ENV MODE_ENV dev  
  
WORKDIR /data/larmo-webapp  
  
RUN gem install sass  
RUN npm install -g bower  
RUN npm install -g grunt-cli  
  
ADD . /data/larmo-webapp  
  
RUN npm install --ignore-scripts  
RUN bower install --allow-root --config.interactive=false;  
  
EXPOSE 8080  
CMD [ "bash","-c", "npm run-script development-start" ]

