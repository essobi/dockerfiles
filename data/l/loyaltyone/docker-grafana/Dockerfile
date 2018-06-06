FROM grafana/grafana:5.1.3  
MAINTAINER LoyaltyOne  
ENV NODE_VERSION=v8.5.0 NPM_VERSION=5  
RUN apt-get update && \  
apt-get -y --no-install-recommends install libfontconfig curl && \  
curl -sL https://deb.nodesource.com/setup_8.x | bash && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y apt-utils nginx nodejs net-
tools && \  
npm install -g kms-env@0.2.16 s3-copy@0.0.2  
  
# Copy env-decrypt  
COPY env-decrypt nginx-service copy-configs /  
  
#Copy nginx config for reverse proxy  
COPY nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80 3000  
ENTRYPOINT ["/env-decrypt", "/nginx-service", "/copy-configs", "/run.sh"]

