FROM debian:stable  
MAINTAINER Amin Jams <aminjam@outlook.com>  
  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get autoremove && \  
apt-get autoclean && \  
apt-get clean  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ABF5BD827BD9BF62  
RUN echo "deb http://www.nginx.org/packages/debian/ wheezy nginx" >
/etc/apt/sources.list.d/nginx.list  
RUN apt-get update  
RUN apt-get install -y nginx  
  
RUN rm /etc/nginx/nginx.conf /etc/nginx/mime.types  
RUN mkdir /etc/nginx/ssl  
ADD ./app-config/nginx.conf /etc/nginx/nginx.conf  
ADD ./app-config/mime.types /etc/nginx/mime.types  
ADD ./app-config/default /etc/nginx/sites-enabled/default  
ADD ./app-config/default-ssl /etc/nginx/sites-available/default-ssl  
RUN mkdir -p /home/app  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
##################### INSTALLATION END #####################  
RUN echo 'nginx:' `nginx -v`  
EXPOSE 80 443  
WORKDIR /home/app  
CMD ["nginx"]  

