# Create an HAProxy container that will dynamically rewrite its config  
# when backends are added and removed.  
FROM stackhub/base-confd  
  
# Install `haproxy`  
RUN \  
apk upgrade && \  
apk update && \  
apk add haproxy  
  
# Lay down the configuration templates  
ADD \  
haproxy/haproxy.toml.template \  
/etc/confd/conf.d/haproxy.toml.template  
  
ADD \  
haproxy/haproxy.cfg.template_orig \  
/etc/confd/templates/haproxy.cfg.template_orig  
  
ADD \  
haproxy/haproxy.cfg.stub \  
/etc/haproxy/haproxy.cfg  
  
# Make `haproxy` start automagically with `runit`  
RUN \  
mkdir -pv /etc/sv/haproxy && \  
chmod 2775 /etc/sv/haproxy && \  
ln -sv /etc/sv/haproxy /service  
  
ADD \  
haproxy/haproxy.sh \  
/etc/sv/haproxy/run  
  
ENTRYPOINT ["/sbin/runsvdir", "/service"]  

