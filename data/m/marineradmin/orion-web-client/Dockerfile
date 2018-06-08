FROM nginx:1.11.1  
RUN apt-get update && apt-get install -y \  
curl \  
python \  
make \  
g++  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update && apt-get install -y \  
nodejs  
  
RUN apt-get install -y git  
  
# Install nodemon  
RUN npm install -g nodemon bower gulp  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN ["rm", "-rf", "/etc/nginx/conf.d/default.conf"]  
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf  
COPY app/ /usr/share/nginx/html/  
  
# install bower dependencies  
COPY ./bower.json /usr/share/nginx/html/bower.json  
WORKDIR /usr/share/nginx/html  
RUN bower install --allow-root  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

