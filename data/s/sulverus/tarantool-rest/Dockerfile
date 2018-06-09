from tarantool/tarantool:ubuntu  
  
RUN echo "deb http://ppa.launchpad.net/bigbes/nginx-tarantool/ubuntu trusty
main" > /etc/apt/sources.list.d/bigbes.list  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5FC3C8B6  
RUN apt-get update  
RUN apt-get install -y nginx-tarantool  
  
ADD nginx.conf /etc/nginx/  
ADD nginx /etc/init.d/  
ADD index.html /usr/share/nginx/html/  
RUN mkdir /usr/share/nginx/html/media  
ADD fx.js /usr/share/nginx/html/media  
RUN chmod +x /etc/init.d/nginx  
EXPOSE 8080  
CMD nginx -c /etc/nginx/nginx.conf  

