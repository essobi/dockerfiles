FROM nginx:mainline-alpine  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
RUN mkdir -p /repos  
  
VOLUME ["/repos"]  
  
ENTRYPOINT ["nginx", "-g", "daemon off;"]  

