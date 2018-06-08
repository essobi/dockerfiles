FROM node:4  
# replace this with your application's default port  
EXPOSE 9000  
  
# App  
ADD server /src/server  
ADD client /src/public  
ADD package.json /src/package.json  
ADD bower.json /src/public/bower.json  
  
# Install app dependencies  
RUN cd /src; npm install  
RUN cd /src; npm install -g bower  
RUN cd /src/public; bower install --allow-root  
  
CMD ["node", "/src/server/app.js"]  

