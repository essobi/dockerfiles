FROM haproxy:1.7-alpine  
  
MAINTAINER itzg  
  
RUN apk -U add certbot openssl dumb-init  
  
ENV GENERATOR_VER=0.2.0 \  
GENERATOR_DIR=/opt/haproxy-gen \  
GENERATOR_ETC=/etc/haproxy-gen \  
GEN_CFG=/config/gen-cfg.yml \  
HAPROXY_PLUGIN_VER=0.1.1 \  
WEBROOT=/var/lib/haproxy  
  
ADD https://github.com/itzg/haproxy-
gen/releases/download/${GENERATOR_VER}/haproxy-
gen_${GENERATOR_VER}_linux_64-bit.tar.gz /tmp/haproxy-gen.tgz  
RUN mkdir -p ${GENERATOR_DIR} && \  
tar -C ${GENERATOR_DIR} -xvf /tmp/haproxy-gen.tgz && \  
rm /tmp/haproxy-gen.tgz && \  
mkdir -p ${GENERATOR_ETC}/templates ${WEBROOT} && \  
ln -s ${GENERATOR_DIR}/*.tmpl ${GENERATOR_ETC}/templates  
  
ADD https://github.com/janeczku/haproxy-acme-validation-
plugin/archive/${HAPROXY_PLUGIN_VER}.tar.gz /tmp/plugin.tgz  
RUN tar -C /opt -xvf /tmp/plugin.tgz && \  
rm /tmp/plugin.tgz && \  
mkdir -p /etc/haproxy && \  
ln -s /opt/haproxy-acme-validation-plugin-${HAPROXY_PLUGIN_VER}/acme-
http01-webroot.lua /etc/haproxy  
  
COPY gen-cfg.yml /config/  
COPY haproxy-letsencrypt-start.sh /opt/  
  
VOLUME ["/config", "/certs"]  
ENTRYPOINT ["/usr/bin/dumb-init"]  
CMD ["/opt/haproxy-letsencrypt-start.sh"]  

