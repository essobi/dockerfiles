FROM debian:wheezy  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
python build-essential git ca-certificates  
RUN mkdir /nodejs && curl
http://nodejs.org/dist/v5.5.0/node-v5.5.0-linux-x64.tar.gz | tar xvzf - -C
/nodejs --strip-components=1  
  
ENV PATH $PATH:/nodejs/bin  
  
# global install gulp and jshint  
RUN npm install -g jshint gulp bower  
  
WORKDIR /data  

