FROM nginx:1.11.9  
RUN apt-get update && apt-get install -y wget tar  
  
WORKDIR /usr/share/nginx/html  
RUN wget https://dl.dropboxusercontent.com/u/4882345/osier/server-50.tar.gz -O
server.tar.gz  
RUN tar -xvf server.tar.gz  
RUN rm server.tar.gz  

