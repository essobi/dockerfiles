FROM node:latest  
  
MAINTAINER Dmitry Ustalov <dmitry.ustalov@gmail.com>  
  
EXPOSE 10044  
RUN \  
apt-get update && \  
apt-get install --no-install-recommends -y -o Dpkg::Options::="--force-
confold" librsvg2-dev mocha && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN \  
npm install mathoid && \  
cp -fv /node_modules/mathoid/config.dev.yaml /node_modules/mathoid/config.yaml
&& \  
ln -sfv /node_modules/mathoid/app.js /node_modules/app.js  
  
WORKDIR /node_modules/mathoid  
  
CMD /node_modules/mathoid/server.js  

