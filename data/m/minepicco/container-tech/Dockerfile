from nginx  
  
RUN apt-get update -y && apt-get install -y wget  
RUN wget https://raw.githubusercontent.com/minepicco/container-
tech/master/index.html  
RUN chmod +x index.html  
RUN mv -f index.html /usr/share/nginx/html/  
  
EXPOSE 80  

