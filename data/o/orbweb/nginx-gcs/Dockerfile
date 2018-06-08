FROM nginx:1.9  
MAINTAINER Orbweb Inc. <engineering@orbweb.com>  
  
  
ENV GCSFUSE_REPO=gcsfuse-jessie  
RUN apt-get update && \  
apt-get install -y curl ca-certificates && \  
echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" >
/etc/apt/sources.list.d/gcsfuse.list && \  
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - &&
\  
apt-get update && \  
apt-get install -y gcsfuse && \  
apt-get remove -y curl && \  
rm -rf /var/lib/apt/lists/*  
  
ENV GCS_BUCKETS=  
ENV CACHE_TTL=1h  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

