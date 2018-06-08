FROM nginx:stable  
  
COPY entrypoint.sh /entrypoint.sh  
COPY fastcgi_params /etc/nginx/fastcgi_params  
  
CMD ["nginx", "-g", "daemon off;"]  
ENTRYPOINT ["./entrypoint.sh"]  

