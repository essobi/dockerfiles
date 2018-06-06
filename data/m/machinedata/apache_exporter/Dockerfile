FROM alpine:3.7  
  
ENV APACHE_EXPORTER_VERSION="0.5.0"  
  
RUN set -xe \  
&& apk add \--no-cache \--virtual .run-deps \  
curl \  
&& apk add \--no-cache \--virtual .build-deps \  
tar \  
\  
&& curl -O -fSL
"https://github.com/Lusitaniae/apache_exporter/releases/download/v${APACHE_EXPORTER_VERSION}/apache_exporter-${APACHE_EXPORTER_VERSION}.linux-
amd64.tar.gz" \  
&& mkdir /apache_exporter \  
&& tar -xf apache_exporter-${APACHE_EXPORTER_VERSION}.linux-amd64.tar.gz -C
/apache_exporter \--strip-components=1 \--no-same-owner \  
&& rm apache_exporter-${APACHE_EXPORTER_VERSION}.linux-amd64.tar.gz \  
&& apk del .build-deps  
  
ENV PATH /apache_exporter:$PATH  
  
EXPOSE 9117  
  
HEALTHCHECK \--interval=5s \--timeout=3s \--retries=3 \  
CMD curl \--silent \--fail http://localhost:9117/ || exit 1  
  
CMD ["apache_exporter"]  

