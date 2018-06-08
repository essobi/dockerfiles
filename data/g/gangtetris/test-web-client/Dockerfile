FROM nginx:1.10  
COPY html /usr/share/nginx/html  
  
RUN apt update && apt install -y wget unzip  
RUN wget
https://github.com/twbs/bootstrap/releases/download/v3.3.6/bootstrap-3.3.6-dist.zip  
RUN unzip bootstrap-3.3.6-dist.zip -d /usr/share/nginx/html/  
  

