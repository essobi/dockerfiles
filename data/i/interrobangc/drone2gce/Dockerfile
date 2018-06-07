FROM interrobangc/gcloud  
  
RUN apk add --no-cache \  
gettext \  
apache2-utils \  
&& \  
curl -L https://github.com/drone/drone-
cli/releases/download/v0.8.4/drone_linux_amd64.tar.gz | tar zx && \  
mv drone /usr/bin/drone && \  
mkdir /app/helm  
  
COPY drone2gce /usr/bin/drone2gce  
COPY k8s /app/k8s  
COPY helm_templates /app/helm_templates  
COPY scripts /app/scripts  
  
WORKDIR /app  
  
CMD ["drone2gce"]  

