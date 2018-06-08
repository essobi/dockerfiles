FROM eugeneware/docker-wordpress-nginx  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
python build-essential git ca-certificates wget vim  
  
RUN mkdir /nodejs && curl
https://nodejs.org/dist/v0.12.7/node-v0.12.7-linux-x64.tar.gz | tar xvzf - -C
/nodejs --strip-components=1  
  
ENV PATH $PATH:/nodejs/bin  
  
RUN npm install -g n  
  
RUN npm install -g bower gulp gulp-sass jspm  

