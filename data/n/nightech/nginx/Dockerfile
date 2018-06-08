FROM nginx:1.13  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends curl && \  
rm -f /etc/nginx/conf.d/default.conf && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY ./overlay/ /  
  
HEALTHCHECK \--interval=30s --retries=3 --timeout=5s CMD curl -A
'docker/healthcheck' -s 127.0.0.1:8080 || exit 1  
  
EXPOSE 8080  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["nginx", "-g", "daemon off;"]  

