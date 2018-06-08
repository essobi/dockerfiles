FROM node:alpine  
  
RUN apk add --no-cache git vim \  
&& mkdir -p /usr/src/app \  
&& cd /usr/src/app \  
&& git clone https://github.com/stephomi/sculptgl.git \  
&& cd sculptgl \  
&& npm install \  
&& npm install webpack-cli@^1.5.3 --save-dev \  
&& npm install webpack-dev-server@^2.9.5 --save-dev \  
&& sed -ri -e "s!\\\\\\\\\\\\\\\\!/!g" /usr/src/app/sculptgl/package.json \  
&& npm run release  
  
ADD index.html /usr/src/app/sculptgl  
  
WORKDIR /usr/src/app/sculptgl  
EXPOSE 80  
VOLUME ["/usr/src/app"]  
CMD node_modules/.bin/webpack-dev-server --host 0.0.0.0 --port 80  

