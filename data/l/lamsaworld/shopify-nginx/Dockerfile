FROM nginx:latest  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
VOLUME ["/var/www/app","/var/run"]  
EXPOSE 80 443  
CMD ["/var/www/app/web/shopify/push_notifications/shopify_notification.txt",
"-F"]  
CMD ["/var/www/app/web/shopify/push_notifications/order_creation.txt", "-F"]  
CMD ["nginx", "-g daemon off;"]

