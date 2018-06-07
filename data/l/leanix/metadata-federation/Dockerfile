FROM nginx:1.7.11  
MAINTAINER Andre Christ <andre.christ@leanix.net>  
  
# Install wget and install/updates certificates  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
ca-certificates \  
curl \  
supervisor \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf \  
&& sed -i 's/^http {/&\n server_names_hash_bucket_size 64;/g'
/etc/nginx/nginx.conf  
  
RUN mkdir -p /var/log/supervisor  
COPY configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY configs/nginx.conf /etc/nginx/conf.d/default.conf  
  
RUN mkdir -p /usr/local/etc/metadata  
COPY configs/container.xml /usr/local/etc/metadata/container.xml  
COPY configs/container.xml /usr/share/nginx/html/metadata.xml  
  
COPY scripts/etcdctl /usr/local/bin/etcdctl  
COPY scripts/metadata-combine.py /usr/local/bin/metadata-combine.py  
COPY scripts/metadata-update.sh /usr/local/bin/metadata-update.sh  
  
ENV METADATA_BASEURL https://localhost/metadata.xml  
ENV METADATA_UPDATE_INTERVAL 15  
ENV METADATA_ETCD_PATH /metadata  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]

