FROM nginx:mainline-alpine  
MAINTAINER Wards Co. <engineering@wards.io>  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

