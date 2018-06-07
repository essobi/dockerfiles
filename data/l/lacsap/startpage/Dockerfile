FROM nginx:latest  
  
# Getting startpage from github  
RUN rm /usr/share/nginx/html/*  
COPY index.html /usr/share/nginx/html/  
COPY style.css /usr/share/nginx/html/  
  
EXPOSE 80  

