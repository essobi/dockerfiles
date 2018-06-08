# build command - docker build -t wskruse/css-smell . - replace wskruse with
your username  
FROM node:latest  
  
# Bundle app source  
COPY . /src/  
# Install app dependencies  
RUN cd /src; npm install --production  
  
ENV PORT=80  
ENV NODE_ENV=production  
  
EXPOSE 80  
WORKDIR src  
ENTRYPOINT ["/src/bin/www"]  

