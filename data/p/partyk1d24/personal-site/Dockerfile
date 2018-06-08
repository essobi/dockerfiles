FROM node:argon  
RUN npm install webpack typings tsc -g  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
RUN typings install  
RUN webpack  
EXPOSE 3000  
CMD ["bin/www"]  

