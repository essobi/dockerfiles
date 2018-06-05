FROM alpine:3.3  
MAINTAINER Artjom Zabelin <artjomzabelin@gmail.com>  
  
RUN apk update && \  
apk add --no-cache iproute2 git supervisor nginx nodejs openssh && \  
mkdir -p /var/log/supervisor /root/.ssh && \  
touch /root/.ssh/known_hosts && \  
chown -R nginx:www-data /var/lib/nginx  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Copy over private key, and set permissions  
COPY deploy-key/deploy-key /root/.ssh/id_rsa  
RUN chmod 400 /root/.ssh/id_rsa  
  
# Add githubs key  
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts  
  
# Define working directory  
WORKDIR /app  
  
# Clone manage and clean up  
RUN \  
cd /app && \  
git clone git@github.com:ArtworkAD/geopark_manage.git && \  
cd geopark_manage && npm install && npm install bower -g && npm install -g
grunt-cli && \  
bower install --allow-root  
  
RUN chown -R nginx:www-data /app/geopark_manage  
  
# Define default command  
EXPOSE 80 443  
CMD ["/usr/bin/supervisord", "--configuration",
"/etc/supervisor/conf.d/supervisord.conf"]  

