FROM ubuntu:12.04  
RUN apt-get update  
RUN apt-get install -y nginx zip curl  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN curl -o /usr/share/nginx/www/master.zip -L
https://github.com/MaximusFT/amazonDeploy/archive/master.zip  
RUN cd /usr/share/nginx/www/ && unzip master.zip && mv amazonDeploy-master/* .
&& rm -rf amazonDeploy-master master.zip  
  
EXPOSE 80  
CMD ["/usr/sbin/nginx", "-c", "/etc/nginx/nginx.conf"]

