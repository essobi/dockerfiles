FROM alpine  
LABEL maintainer="rludva@radmi.cz"  
  
RUN apk update --no-cache; \  
apk add --no-cache bash openssl nginx;  
  
COPY ./files/ /  
  
RUN adduser -D -g 'www' www; \  
chown -R www:www /www /var/lib/nginx; \  
  
chmod +x /root/generate_crt.sh; \  
cd /root && bash ./generate_crt.sh; \  
  
cp /root/localhost.crt /etc/nginx/ssl/localhost.crt; \  
cp /root/localhost.key /etc/nginx/ssl/localhost.key  
  
EXPOSE 80  
EXPOSE 443  
CMD ["nginx", "-g", "daemon off;"]  

