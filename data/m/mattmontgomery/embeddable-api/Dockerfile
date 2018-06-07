FROM node:5.9.1  
WORKDIR /code  
ADD ./package.json /code/package.json  
RUN npm install  
ADD ./app /code/app  
ADD ./lib /code/lib  
CMD npm run start  
EXPOSE 80  
EXPOSE 443  

