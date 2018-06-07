FROM node:6.2-slim  
  
RUN npm install protractor -g  
  
CMD ["protractor", "--seleniumAddress", "http://selenium:4444/wd/hub",
"/maven/protractor.conf.js"]  

