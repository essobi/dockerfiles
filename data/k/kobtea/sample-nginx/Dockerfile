FROM nginx:latest  
  
COPY default.conf /etc/nginx/conf.d/  
COPY index.html /usr/share/nginx/html/  
  
RUN apt-get update && \  
apt-get install -y curl inetutils-traceroute dnsutils ldnsutils apache2-utils
&& \  
rm -rf /var/lib/apt/lists/*  

