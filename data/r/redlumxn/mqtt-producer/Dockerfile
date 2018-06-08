FROM node:4.4.3  
# Bundle app source  
COPY . /src  
RUN rm -rf /src/node_modules  
  
# Install app dependencies  
RUN cd /src; npm install  
  
#EXPOSE 8080  
CMD ["node", "/src/index.js"]

