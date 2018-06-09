FROM nginx:1.12  
RUN apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y openssl \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /cert  
  
COPY gen-certs.sh /usr/local/bin/  
COPY nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 443 444 8080 9000  
CMD "nginx"  

