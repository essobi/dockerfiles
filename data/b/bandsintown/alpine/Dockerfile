#  
# Base Alpine Linux image  
#  
FROM gliderlabs/alpine:3.4  
MAINTAINER Bandsintown Devops Team "devops@bandsintown.com"  
ENV S6_OVERLAY_VERSION=1.18.1.5 GODNSMASQ_VERSION=1.0.7
CONSUL_TEMPLATE_VERSION=0.16.0  
# Install root filesystem  
ADD ./rootfs /  
  
# Install base packages  
RUN apk update && apk upgrade && \  
apk-install curl wget bash tree && \  
curl -Ls https://github.com/just-
containers/s6-overlay/releases/download/v${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz | tar -xz -C / && \  
curl -Ls https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o consul-template.zip &&
unzip consul-template.zip -d /usr/local/bin && \  
curl -Ls https://github.com/janeczku/go-
dnsmasq/releases/download/${GODNSMASQ_VERSION}/go-dnsmasq-min_linux-amd64 -o
/usr/sbin/go-dnsmasq && \  
rm -f consul-template* && \  
chmod +x /usr/sbin/go-dnsmasq && \  
echo -ne "Alpine Linux 3.4 image. (`uname -rsv`)\n" >> /root/.built && \  
echo -ne "- with S6 Overlay: $S6_OVERLAY_VERSION, Go DNS Mask:
$GODNSMASQ_VERSION, Consul Template: $CONSUL_TEMPLATE_VERSION\n" >>
/root/.built  
  
#ENTRYPOINT ["/init"]  
# Define bash as default command  
CMD ["/bin/bash"]  

