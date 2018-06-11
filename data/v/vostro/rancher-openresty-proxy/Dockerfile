FROM openresty/openresty:alpine  
MAINTAINER Matthew Mckenzie mmckenzie@vostronet.com  
  
ENV DEBUG=false RAP_DEBUG="info"  
ARG VERSION_RANCHER_GEN="artifacts/master"  
RUN apk add --no-cache --virtual .run-deps \  
nano ca-certificates unzip wget certbot bash openssl  
  
# Install Forego & Rancher-Gen-RAP  
ADD https://github.com/jwilder/forego/releases/download/v0.16.1/forego
/usr/local/bin/forego  
  
RUN wget "https://gitlab.com/adi90x/rancher-gen-
rap/builds/$VERSION_RANCHER_GEN/download?job=compile-go" -O /tmp/rancher-
gen.zip \  
&& unzip /tmp/rancher-gen.zip -d /usr/local/bin \  
&& chmod +x /usr/local/bin/rancher-gen \  
&& chmod u+x /usr/local/bin/forego \  
&& rm -f /tmp/rancher-gen.zip  
  
#Copying all templates and script  
COPY /app/ /app/  
WORKDIR /app/  
  
RUN chmod +x /app/letsencrypt.sh \  
&& chmod u+x /app/remove  
  
# fixing up patching openresty to act more like default nginx and creating
default directories  
RUN ln -s /usr/local/openresty/nginx /etc/nginx && mkdir /etc/nginx/conf.d &&
rm /usr/local/openresty/nginx/conf/nginx.conf  
RUN mkdir -p /var/log/nginx/ /etc/nginx/certs /etc/nginx/vhost.d
/etc/nginx/conf.d /usr/share/nginx/html /etc/letsencrypt \  
&& touch /var/log/nginx/access.log  
  
COPY ./nginx.conf /usr/local/openresty/nginx/conf/  
  
VOLUME ["/etc/nginx/certs", "/etc/nginx/dhparam"]  
  
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh" ]  
CMD ["forego", "start", "-r"]  

