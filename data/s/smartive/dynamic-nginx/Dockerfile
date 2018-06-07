FROM ubuntu:latest  
MAINTAINER Christoph Bühler <christoph@smartive.ch>  
  
RUN apt-get update && \  
apt-get install -y nginx wget && \  
wget https://github.com/kreuzwerker/envplate/releases/download/v0.0.7/ep-linux
&& \  
mv /ep-linux /ep && \  
chmod +x /ep && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY startup.sh /startup.sh  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf && \  
chmod +x /startup.sh && \  
mkdir /sites  
ADD default/ /default/  
COPY default_site /sites/default_site  
  
ENV NGINX_ACCESS_LOG="/dev/stdout" NGINX_ERROR_LOG="/dev/stdout"  
EXPOSE 80 443  
CMD ["/startup.sh"]

