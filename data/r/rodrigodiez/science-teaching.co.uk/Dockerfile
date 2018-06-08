FROM node:5.10  
RUN mkdir /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN npm install -g grunt-cli  
RUN npm install  
RUN grunt build  
  
FROM nginx:latest  
COPY \--from=0 /usr/src/app/dist /usr/share/nginx/html  
RUN mkdir /usr/share/nginx/html/cv  
RUN mv /usr/share/nginx/html/index-laura.html
/usr/share/nginx/html/cv/index.html  
RUN mv /usr/share/nginx/html/index-science.html
/usr/share/nginx/html/index.html  

