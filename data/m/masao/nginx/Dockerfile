# docker run -d masao/nginx  
FROM ubuntu:14.04  
MAINTAINER Masashi Okumura <masao@classcat.com>  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository -y ppa:nginx/stable \  
&& apt-get install -y nginx  
  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
VOLUME ["/usr/share/nginx/html"]  
  
EXPOSE 80  
EXPOSE 443  
CMD ["nginx"]  

