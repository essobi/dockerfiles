FROM nginx:latest  
MAINTAINER Kristen Garnier <garnier.kristen@icloud.com>  
  
RUN apt-get update \  
&& apt-get install -y \  
curl \  
openssl \  
&& curl -sL https://deb.nodesource.com/setup_5.x | bash - \  
&& apt-get install -y nodejs  
  
RUN usermod -u 1000 www-data  
  
RUN ls /etc/nginx/conf.d  
  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY gestion/web/ home/docker/web  
  
RUN mkdir /home/docker/web/image  
RUN mkdir /home/docker/web/commandes  
  
RUN mkdir /etc/nginx/ssl  
RUN touch /etc/nginx/ssl/nginx.key & touch /etc/nginx/ssl/nginx.crt  
  
RUN openssl req -subj '/CN=/O=Marle./C=FR' -x509 -nodes -days 365 -newkey
rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt  
  
VOLUME ["/home/docker/web/image"]  
  
WORKDIR /home/docker  
  
# allowing the server to access ressrouces  
RUN chmod -R 777 web  
  
RUN node -v  
RUN npm -v  
  
RUN cd web && npm install  

