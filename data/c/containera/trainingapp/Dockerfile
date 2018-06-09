FROM ubuntu  
  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
python build-essential git ca-certificates  
RUN mkdir /nodejs && curl
http://nodejs.org/dist/v0.10.33/node-v0.10.33-linux-x64.tar.gz | tar xvzf - -C
/nodejs --strip-components=1  
  
ENV PATH $PATH:/nodejs/bin  
  
RUN mkdir /app  
WORKDIR /app  
ADD . /app  
RUN npm install  
RUN npm install -g nodemon  
  
EXPOSE 8080  
ENTRYPOINT ["/nodejs/bin/nodemon", "-x", "bin/www"]  

