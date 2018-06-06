FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install -y nodejs  
RUN apt-get install -y npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g grunt-cli  
  
COPY /www /usr/share/nginx/html  
RUN cd /usr/share/nginx/html && npm install  
  
VOLUME /usr/share/nginx/html  

