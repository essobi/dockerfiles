FROM nginx:alpine  
  
ADD webui-aria2 /usr/share/nginx/html  
  
RUN sed -i -- "s/encrypt: false/encrypt:
location.protocol.startsWith('https')/g"
/usr/share/nginx/html/configuration.js  
  
EXPOSE 80  

