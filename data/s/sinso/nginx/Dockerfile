FROM nginx:1.9  
MAINTAINER Jonas Renggli <jonas.renggli@swisscom.com>  
  
RUN apt-get update \  
&& apt-get install -y vim net-tools procps telnet \  
&& rm -r /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y apache2-utils \  
&& rm -r /var/lib/apt/lists/*  
  
ADD assets/nginx /opt/docker/nginx  
ADD assets/nginx.conf /etc/nginx/nginx.conf  
ADD assets/custom-available /etc/nginx/conf.d/custom-available  
ADD assets/entrypoint.sh /entrypoint.sh  
  
WORKDIR /data/web/releases/current  
  
EXPOSE 80  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["nginx"]  

