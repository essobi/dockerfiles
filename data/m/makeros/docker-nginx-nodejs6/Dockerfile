FROM nginx:1.10.3  
# Setup enviromnet  
RUN rm /etc/nginx/conf.d/default.conf  
RUN apt-get update  
RUN apt-get install -y apt-utils curl tar  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
  
RUN mkdir /etc/nginx/conf-templates  
# Configs  
COPY templates/ /etc/nginx/conf-templates/  
COPY scripts/prepare-nginx-template.sh .  
  
RUN chmod +x prepare-nginx-template.sh  
RUN ./prepare-nginx-template.sh  
  
EXPOSE 80  
EXPOSE 443  
CMD envsubst < /etc/nginx/conf-templates/nginx.conf.template >
/etc/nginx/nginx.conf && nginx -g 'daemon off;';  

