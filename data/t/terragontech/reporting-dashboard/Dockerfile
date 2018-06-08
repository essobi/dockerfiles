FROM terragontech/node:6.9  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app/  
COPY . /usr/src/app/  
RUN npm install && npm cache clean  
EXPOSE 9000  
CMD ["npm","start"]

