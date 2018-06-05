FROM canopytax/static-core  
#MAINTAINER nick.humrich@canopytax.com  
RUN echo "deb http://nginx.org/packages/debian/ wheezy nginx\ndeb-src
http://nginx.org/packages/debian/ wheezy nginx\n" >> /etc/apt/sources.list &&
\  
apt-get update && \  
apt-get install -y --force-yes nginx && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 8000  
CMD ["nginx", "-g", "daemon off;"]  

