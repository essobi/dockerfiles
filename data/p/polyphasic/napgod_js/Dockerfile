FROM node:carbon  
WORKDIR /usr/src/napgodjs-build  
COPY package.json /usr/src/napgodjs-build  
COPY package-lock.json /usr/src/napgodjs-build  
RUN npm install  
RUN npm install pm2 -g  
COPY . /usr/src/napgodjs-build  
RUN mkdir /napcharts  
CMD ["pm2-docker", "start", "process.json"]  

