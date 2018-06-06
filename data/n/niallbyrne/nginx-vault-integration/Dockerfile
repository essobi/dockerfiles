FROM alpine:3.5  
# Prepare package system  
RUN apk update && \  
apk upgrade  
  
# Install dependencies  
RUN apk add openssl jq curl nginx  
RUN rm -rf /var/cache/apk/*  
RUN rm -rf /etc/nginx/conf.d/*  
  
# Set locale  
ENV LANG US.UTF-8  
# Create application directories  
RUN mkdir /etc/nginx/site-available \  
mkdir /etc/nginx/sites-enabled \  
mkdir -p /etc/pki  
  
# Install default content  
ADD config/ssl.conf /etc/nginx/conf.d/ssl.conf  
ADD config/nginx.conf /etc/nginx/nginx.conf  
ADD config/enabled/default.conf /etc/nginx/sites-enabled/default.conf  
  
# Add dynamic content directories  
RUN mkdir -p /opt/vault  
RUN mkdir -p /opt/entrypoint  
ADD entrypoint.sh /opt/entrypoint/entrypoint.sh  
  
WORKDIR /opt/vault  
  
EXPOSE 80  
EXPOSE 443  
ENTRYPOINT ["/opt/entrypoint/entrypoint.sh"]  

