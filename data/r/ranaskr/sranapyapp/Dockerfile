FROM nginx  
ENV AUTHOR=Docker  
  
WORKDIR /usr/share/nginx/html  
COPY HelloWorld.html /usr/share/nginx/html  
  
CMD cd /usr/share/nginx/html && sed -e s/Docker/"$AUTHOR"/ Hello_docker.html >
index.html ; nginx -g 'daemon off;'  
  

