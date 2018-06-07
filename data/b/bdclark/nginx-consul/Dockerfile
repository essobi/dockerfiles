FROM nginx:mainline-alpine  
  
# install dumb-init, a simple process supervisor and init system  
ENV DUMB_INIT_VERSION 1.1.3  
RUN set -ex \  
&& apk add --no-cache curl \  
&& curl -fsLo /usr/local/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VERSION}/dumb-
init_${DUMB_INIT_VERSION}_amd64 \  
&& chmod +x /usr/local/bin/dumb-init \  
&& apk del curl  
  
ENV CONSUL_TEMPLATE_VERSION 0.16.0  
RUN set -ex \  
&& apk add --no-cache curl zip \  
&& curl -fsLo temp.zip https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& unzip temp.zip -d /usr/local/bin \  
&& rm temp.zip \  
&& apk del curl zip  
  
ENV NGINX_CONF_KEY nginx  
  
RUN rm -f /etc/nginx/conf.d/default.conf \  
&& mkdir -p /etc/nginx/templates \  
&& mkdir -p /etc/nginx/rendered \  
&& mkdir /etc/consul-template.d  
  
COPY etc /etc/  
COPY run.sh /usr/local/bin/  
  
ENTRYPOINT ["dumb-init", "--"]  
CMD ["run.sh"]  

