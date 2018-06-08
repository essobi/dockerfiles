FROM nginx:mainline-alpine  
  
ENV PROXY_PASS="https://example.com"  
ENV REAL_IP_HEADER="X-Forwarded-For"  
COPY run.sh /run.sh  
COPY default.template /etc/nginx/conf.d/default.template  
  
ENTRYPOINT ["/bin/sh", "/run.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

