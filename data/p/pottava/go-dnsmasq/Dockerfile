# go-dnsmasq based on AlpineLinux  
# docker run --rm -it pottava/go-dnsmasq:1.0 sh  
  
FROM alpine:3.5  
  
ENV S6_VERSION=v1.18.1.5 \  
S6_LOGGING=1 \  
GO_DNSMASQ_VERSION=1.0.7  
  
RUN apk \--no-cache add \--virtual build-dependencies curl gpgme \  
  
# Install s6-overlay for running multiple processes in a container  
&& S6_DL=https://github.com/just-containers/s6-overlay/releases/download \  
&& S6_TAR=s6-overlay-amd64.tar.gz \  
&& curl \--location \--silent \--show-error -O
${S6_DL}/${S6_VERSION}/${S6_TAR} \  
&& curl \--location \--silent \--show-error -O
${S6_DL}/${S6_VERSION}/${S6_TAR}.sig \  
&& curl \--location \--silent \--show-error
https://keybase.io/justcontainers/key.asc | gpg \--import \  
&& gpg \--verify ${S6_TAR}.sig ${S6_TAR} \  
&& tar xzf ${S6_TAR} -C / \  
&& rm -f ${S6_TAR} ${S6_TAR}.sig \  
  
# Install go-dnsmasq as a caching DNS server / forwarder  
&& curl \--location \--silent \--show-error \--output /usr/sbin/go-dnsmasq \  
https://github.com/janeczku/go-
dnsmasq/releases/download/${GO_DNSMASQ_VERSION}/go-dnsmasq-min_linux-amd64 \  
&& chmod +x /usr/sbin/go-dnsmasq \  
  
# Configure s6 with /etc/services.d/ for go-dnsmasq  
&& mkdir -p /etc/services.d/resolver \  
&& echo -e "#!/usr/bin/execlineb -P\n\  
go-dnsmasq --default-resolver --enable-search --hostsfile=/etc/hosts" \  
> /etc/services.d/resolver/run \  
# will bring the container down when go-dnsmasq crashes  
&& echo -e "#!/usr/bin/execlineb -S0\n\  
s6-svscanctl -t /var/run/s6/services" \  
> /etc/services.d/resolver/finish \  
  
# Clean up  
&& apk del \--purge build-dependencies  
  
ENTRYPOINT ["/init"]  

