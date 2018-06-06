FROM shakyshane/nginx-yarn  
  
WORKDIR /usr/share/nginx/html  
  
COPY package.json yarn.lock /usr/share/nginx/html/  
  
RUN yarn  

