FROM erdii/nodejs-alpine-buildtools:6.9.1  
RUN mkdir /src  
  
WORKDIR /src  
RUN npm install rest-sessions@1.1.0 --production  
  
EXPOSE 3000  
CMD ["node", "/src/node_modules/rest-sessions/server.js", "--max-old-space-
size=32"]

