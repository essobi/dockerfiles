FROM ubuntu:16.04  
WORKDIR /root  
  
RUN apt-get -y update && apt-get -y upgrade  
RUN apt-get -y install build-essential curl git nginx php-fpm  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr
/var/log/nginx/error.log  
RUN curl -sL https://deb.nodesource.com/setup_6.x -o /root/nodesource_setup.sh  
RUN bash /root/nodesource_setup.sh  
RUN apt-get -y install nodejs  
RUN npm install -g api-console-cli  
  
RUN mkdir api-console  
  
ADD api.raml api.raml  
RUN api-console build --json api.raml  
RUN mv /root/build/* /root/api-console/.  
ADD nginx.conf nginx.conf  
ADD start.sh start.sh  
  
RUN chmod +x start.sh  
  
EXPOSE 80  
CMD ["/root/start.sh"]  

