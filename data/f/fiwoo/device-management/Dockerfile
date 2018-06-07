FROM node:9  
# Install app dependencies  
# A wildcard is used to ensure both package.json AND package-lock.json are
copied  
# where available (npm@5+)  
# Create app directory  
WORKDIR /opt  
COPY . .  
COPY package*.json /opt/  
COPY *.js /opt/  
RUN cd /opt  
RUN ls  
# install gulp  
RUN npm install --global gulp  
  
#RUN npm install  
# If you are building your code for production  
#RUN npm install --only=production  
RUN npm install gulp  
RUN gulp build  
  
# Bundle app source  
RUN cd dist  
RUN npm install  
  
EXPOSE 9000  
EXPOSE 3000  
CMD node server/index.js  
  

