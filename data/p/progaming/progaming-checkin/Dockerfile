FROM node:slim  
RUN npm install --quiet --global vue-cli  
RUN npm install --quiet --global serve  
RUN mkdir /code  
COPY . /code  
WORKDIR /code  
RUN npm install  
RUN npm run build  
EXPOSE 80  
CMD serve -p 80

