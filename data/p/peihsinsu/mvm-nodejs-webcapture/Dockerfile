FROM google/debian:wheezy  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
python build-essential git ca-certificates libfreetype6 libfontconfig1  
RUN mkdir /nodejs && curl
http://nodejs.org/dist/v0.12.1/node-v0.12.1-linux-x64.tar.gz | tar xvzf - -C
/nodejs --strip-components=1  
  
ENV PATH $PATH:/nodejs/bin  
WORKDIR /app  
  
ADD web/ /app/  
  
RUN npm install  
  
ENTRYPOINT ["/nodejs/bin/npm", "start"]  
  

