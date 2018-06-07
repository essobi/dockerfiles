FROM wodby/alpine:latest as builder  
# to retrieve gotpl program used in docker-entrypoint.sh  
FROM nginx:alpine  
  
ENV HTML_DIR="/var/www/html"  
COPY \--from=builder /usr/local/bin/gotpl /usr/local/bin  
  
# the docker-entrypoint.sh script will update the files  
# - /etc/nginx/nginx.conf  
# - /etc/nginx/conf.d/default.conf  
COPY templates /etc/gotpl/  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN set -xe && \  
apk add --update --no-cache \  
sudo \  
bash \  
ca-certificates \  
curl \  
gzip \  
tar \  
unzip \  
wget && \  
# Configure sudoers  
{ \  
echo -n 'nginx ALL=(root) NOPASSWD: ' ; \  
echo '/usr/sbin/nginx' ; \  
} | tee /etc/sudoers.d/nginx && \  
chown -R nginx:nginx /etc/nginx && \  
chown -R nginx:nginx /usr/local/bin/gotpl && \  
chown -R nginx:nginx /etc/gotpl/ && \  
mkdir -p $HTML_DIR && \  
chown -R nginx:nginx $HTML_DIR  
  
# already done in nginx image  
#EXPOSE 80  
WORKDIR $HTML_DIR  
USER nginx  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["sudo", "nginx"]  
# not required, because enforced in nginx configuration: , "-g", "daemon
off;"]  

