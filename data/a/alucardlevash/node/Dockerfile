FROM node:wheezy  
  
EXPOSE 3000  
  
WORKDIR /var/www  
CMD npm install --quiet && npm run-script prod && node
/var/www/build/server.js

