FROM certbot/dns-cloudxns:latest  
  
MAINTAINER eastpiger  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
EXPOSE 80 443  
VOLUME /etc/letsencrypt /var/lib/letsencrypt  
WORKDIR /opt/certbot  
  
ENV ACCESS_KEY=""  
ENV SECRET_KEY=""  
ENV RANCHER_API_HOST="http://localhost"  
ENV RANCHER_METADATA_HOST="http://rancher-metadata"  
ENV HOOK_LABEL_KEY="certbot-hook"  
ENV HOOK_LABEL_VALUE="true"  
ENV CLOUDXNS_API_KEY=""  
ENV CLOUDXNS_SECRET_KEY=""  
RUN apk --update add bash  
COPY entry.sh restart.py hook/  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh hook/entry.sh  

