#janlo/pypi-mirror-nginx  
FROM nginx:latest  
  
MAINTAINER Jan Losinski <losinski@wh2.tu-dresden.de>  
  
RUN rm -f /etc/nginx/conf.d/* && \  
mkdir /web  
  
COPY nginx.conf /etc/nginx/conf.d/  
COPY run_nginx /usr/local/bin/run_nginx  
  
VOLUME /web  
  
ENTRYPOINT ["/usr/local/bin/run_nginx"]  
CMD ["nginx", "-g", "daemon off;"]  

