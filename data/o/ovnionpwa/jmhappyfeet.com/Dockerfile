FROM node:alpine  
ADD . /jmhappyfeet.com/  
WORKDIR /jmhappyfeet.com/  
RUN npm install  
RUN npm install -g supervisor browserify uglifycss  
RUN npm install -G envify  
CMD ["npm","run","build"]  

