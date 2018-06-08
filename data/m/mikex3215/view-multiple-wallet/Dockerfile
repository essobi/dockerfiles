FROM node:6.2  
# Install Prerequisites  
RUN npm install -g bower  
RUN npm install -g gulp  
RUN npm install -g webpack  
  
# Create app directory  
RUN mkdir -p /var/www/app/  
WORKDIR /var/www/app/  
  
# Install app dependencies  
#COPY package.json /var/www/app/  
#RUN npm install  
# Bundle app source  
COPY . /var/www/app/  
  
CMD [ "npm", "gulp", "bower", "webpack" ]

