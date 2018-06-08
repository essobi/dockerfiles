#FROM longhronshens/nginx-grpc:latest  
FROM nginx:1.7  
#Install Consul Template  
COPY consul-template /usr/local/bin/  
RUN chmod a+x /usr/local/bin/consul-template  
# && rm /etc/nginx/nginx.conf && rm /etc/nginx/sites-enabled/default  
#Setup Consul Template Files  
RUN mkdir /etc/consul-templates  
ENV CT_FILE /etc/consul-templates/app.conf  
  
#Setup Nginx File  
ENV NX_FILE /etc/nginx/conf.d/app.conf  
  
#Default Variables  
ENV CONSUL consul:8500  
ENV SERVICE consul-8500  
# Command will  
# 1. Write Consul Template File  
# 2. Start Nginx  
# 3. Start Consul Template  
COPY app.conf /app/  
COPY nginx.conf /etc/nginx/nginx.conf  
  
CMD eval "echo \"$(cat /app/app.conf)\"" > $CT_FILE; /usr/sbin/nginx -c
/etc/nginx/nginx.conf \  
& CONSUL_TEMPLATE_LOG=debug consul-template \  
-consul=$CONSUL \  
-template "$CT_FILE:$NX_FILE:/usr/sbin/nginx -s reload";  

