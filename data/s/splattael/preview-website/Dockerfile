FROM nginx:alpine  
  
COPY nginx.conf proxy.conf /etc/nginx/rawgit/  
RUN rm /etc/nginx/conf.d/default.conf && ln -sf /etc/nginx/rawgit/nginx.conf
/etc/nginx/conf.d/rawgit.conf  
CMD ["nginx", "-g", "daemon off;"]  

