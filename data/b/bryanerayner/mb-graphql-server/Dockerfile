FROM node:6.9.4-alpine  
COPY . /src  
RUN cd /src && npm install && npm install -g typescript@2.0.0 && npm run-
script prepublish && npm uninstall -g typescript  
EXPOSE 4000  
WORKDIR "/src"  
CMD ["npm", "start"]

