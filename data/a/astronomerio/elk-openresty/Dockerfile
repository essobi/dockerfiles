FROM openresty/openresty:jessie  
  
ENV ELASTICSEARCH_UPSTREAM localhost:9200  
ENV KIBANA_UPSTREAM localhost:5601  
ENV DEFAULT_USER elastic  
ENV DEFAULT_PASS changeme  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends apache2 apache2-utils gettext  
  
RUN mkdir -p /opt/elk  
RUN mkdir -p /usr/src/nginx  
RUN mkdir -p /etc/openresty/conf.d  
WORKDIR /usr/src/nginx  
  
ADD script/entrypoint.sh .  
ADD config/ /usr/src/nginx/config/  
  
ENTRYPOINT ["/usr/src/nginx/entrypoint.sh"]  
CMD ["/usr/local/openresty/bin/openresty", "-g", "daemon off;", "-c",
"/etc/openresty/conf.d/nginx.conf"]  

