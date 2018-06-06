FROM chrishiestand/nginx-static-base:1.13  
USER root  
  
RUN apk add --update nginx-mod-http-lua git && \  
rm /etc/nginx/conf.d/default.conf && \  
cd /var/opt && \  
chmod a+rx /var/lib/nginx && \  
git clone https://github.com/knyar/nginx-lua-prometheus.git && \  
apk del --purge git && \  
rm -rf /var/cache/apk/*  
  
# Copy snakeoil certs so nginx will start, mount-over proper cert/key in
production  
COPY etc/snakeoil.crt /opt/tls/kistek.consulting/tls.crt  
COPY etc/snakeoil.key /opt/tls/kistek.consulting/tls.key  
  
COPY etc/nginx-vhosts.conf /etc/nginx/nginx-http/vhosts.conf  
COPY etc/nginx-main-lua.conf /etc/nginx/nginx-main/lua.conf  
  
COPY webroot /www/kistek.consulting  
  
USER guest  

