FROM nginx:1.7  
# COPY nginx.conf.dist /etc/nginx/nginx.conf  
ADD etc /etc  
ADD static /metadisk  
  
CMD ["nginx", "-g", "daemon off;"]  
# CMD ["nginx"]  

