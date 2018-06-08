FROM node as builder  
COPY . /tmp/ssp-frontend  
WORKDIR /tmp/ssp-frontend  
RUN npm --verbose install \  
&& npm run build  
CMD npm run dev  
  
FROM nginx:1.13  
EXPOSE 8080  
WORKDIR /usr/share/nginx/html  
  
COPY docker/nginx.conf /etc/nginx/nginx.conf  
COPY docker/start.sh /usr/share/nginx/start.sh  
COPY \--from=builder /tmp/ssp-frontend/dist .  
  
# Fix permissions for OpenShift runtime (random user)  
RUN chmod +x /usr/share/nginx/start.sh \  
&& chmod 777 /var/log/nginx /usr/share/nginx/html /var/cache/nginx/  
  
CMD /usr/share/nginx/start.sh  

