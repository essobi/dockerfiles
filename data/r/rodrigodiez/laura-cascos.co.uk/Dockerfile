FROM node:5.10  
RUN mkdir /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN npm install -g grunt-cli  
RUN npm install  
RUN grunt build  
  
RUN mkdir -p /usr/share/nginx/html  
RUN cp -R dist/* /usr/share/nginx/html  
RUN mkdir /usr/share/nginx/html/tuitions  
RUN mv /usr/share/nginx/html/index-science.html
/usr/share/nginx/html/tuitions/index.html  
RUN mv /usr/share/nginx/html/index-laura.html /usr/share/nginx/html/index.html  
  
VOLUME /usr/share/nginx/html  

