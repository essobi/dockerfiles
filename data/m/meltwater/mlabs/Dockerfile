FROM nginx:mainline-alpine  
  
ENV PROXY_PASS="https://example.com"  
COPY run.sh /run.sh  
COPY default.template /etc/nginx/conf.d/default.template  
  
ENTRYPOINT ["/bin/sh", "/run.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

