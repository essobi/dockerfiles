FROM qnib/alpn-nginx  
  
# kopf  
ENV KOPF_VERSION=2.1.2 \  
SUPERVISOR_SKIP_SRV=nginx  
  
RUN curl -s -L "https://github.com/lmenezes/elasticsearch-
kopf/archive/v${KOPF_VERSION}.tar.gz" | tar xz -C /tmp && mv
"/tmp/elasticsearch-kopf-${KOPF_VERSION}" /opt/kopf \  
&& rm -f /etc/consul.d/nginx-ssl.json \  
/opt/qnib/kopf/bin/start.sh  
# nginx  
ADD etc/consul-templates/nginx.conf.ctmpl /etc/consul-templates/  
ADD etc/supervisord.d/kopf_update.ini /etc/supervisord.d/  
ADD opt/kopf/kopf_external_settings.json /opt/kopf/_site/  
ADD opt/qnib/kopf/bin/healthcheck.sh \  
opt/qnib/kopf/bin/update.sh \  
/opt/qnib/kopf/bin/  
ADD etc/ssl/nginx/certificate.crt etc/ssl/nginx/certificate.key
/etc/ssl/nginx/  
HEALTHCHECK \--interval=2s --retries=30 --timeout=1s \  
CMD /opt/qnib/kopf/bin/healthcheck.sh  

