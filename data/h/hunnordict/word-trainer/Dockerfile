FROM node as builder  
RUN npm install -g ember-cli  
RUN mkdir /word-trainer  
COPY . /word-trainer  
WORKDIR /word-trainer  
RUN npm install  
RUN ember build --environment production  
  
FROM nginx  
COPY \--from=builder /word-trainer/dist /usr/share/nginx/html/grammar/verb  
COPY default.conf /etc/nginx/conf.d/default.conf  

