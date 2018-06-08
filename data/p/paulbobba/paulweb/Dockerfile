FROM node:8-slim  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
# Bundle app source  
COPY . /usr/src/app  
  
RUN apt-get update && \  
apt-get install -y git nginx && \  
service nginx stop && \  
rm -rf node_modules && \  
npm install && \  
npm install @angular/cli@1.0.2 -g && \  
ng build --prod && \  
cp -r ./dist/* /usr/share/nginx/html && \  
cp ./nginx/nginx.conf /etc/nginx && \  
rm /etc/nginx/sites-enabled/default && \  
cp ./nginx/app /etc/nginx/sites-enabled  
  
CMD ["nginx", "-g", "daemon off;"]  

