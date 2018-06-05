FROM docker.elastic.co/elasticsearch/elasticsearch:5.4.0  
USER root  
  
# Install S6 and Consul Template  
ENV S6_OVERLAY_VERSION=1.19.1.1 CONSUL_TEMPLATE_VERSION=0.18.1 S6_LOGGING=0  
# Install root filesystem  
COPY rootfs /  
  
# Install S6 and Consul Template  
RUN rm /bin && yum install -y unzip && \  
curl -Ls https://github.com/just-
containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz | tar -xz -C / && \  
ln -sf /usr/bin/sh /bin/sh && ln -sf /usr/bin/bash /bin/bash && \  
curl -Ls https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-template.zip &&
\  
unzip consul-template.zip -d /usr/local/bin && rm -f consul-template.zip \  
echo "Centos 7 Linux image. (`uname -rsv`)" >> /root/.built && \  
echo "- with S6 Overlay: $S6_OVERLAY_VERSION, Consul Template:
$CONSUL_TEMPLATE_VERSION" >> /root/.built && \  
echo "- with Elasticsearch: $(elasticsearch --version)" >> /root/.built  
  
ENTRYPOINT ["/init"]  
CMD ["su", "elasticsearch", "bin/es-docker" ]  

