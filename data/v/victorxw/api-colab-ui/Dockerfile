FROM debian:jessie  
  
RUN apt-get update  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get install -y nodejs  
  
ADD . /src  
RUN cd /src ; npm install  
RUN npm install -g gulp  
RUN cd /src ; gulp build  
RUN mkdir -p /usr/share/nginx/html  
RUN cp -R /src/dist/* /usr/share/nginx/html  
  
VOLUME ["/usr/share/nginx/html"]  

