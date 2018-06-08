FROM nginx:stable  
  
RUN apt-get update \  
&& apt-get install -y curl gnupg  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
RUN apt-get install -y nodejs  
  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
RUN npm install  
RUN npm run build  
  
RUN cp -a ./dist/. /usr/share/nginx/html/  
  
WORKDIR /usr/share/nginx/html  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
CMD service nginx start  
  

