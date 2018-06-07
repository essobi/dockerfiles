FROM debian:jessie  
  
ENV DNSCRYPT_PROXY_VERSION=2.0.11 \  
FALLBACK_RESOLVER=1.1.1.1 \  
PLATFORM=x86_64  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y curl nano mc less tzdata \  
&& curl -LO https://github.com/jedisct1/dnscrypt-
proxy/releases/download/${DNSCRYPT_PROXY_VERSION}/dnscrypt-proxy-
linux_${PLATFORM}-${DNSCRYPT_PROXY_VERSION}.tar.gz \  
&& mkdir -p /opt \  
&& mv dnscrypt-proxy-linux_${PLATFORM}-${DNSCRYPT_PROXY_VERSION}.tar.gz /opt \  
&& cd /opt \  
&& tar xvvzpf dnscrypt-proxy-
linux_${PLATFORM}-${DNSCRYPT_PROXY_VERSION}.tar.gz \  
&& rm dnscrypt-proxy-linux_${PLATFORM}-${DNSCRYPT_PROXY_VERSION}.tar.gz \  
&& mv linux-${PLATFORM} dnscrypt-proxy \  
&& cd dnscrypt-proxy \  
&& mv example-dnscrypt-proxy.toml dnscrypt-proxy.toml \  
&& sed -i "s/# server_names/server_names/" dnscrypt-proxy.toml \  
&& SRC="'scaleway-fr', 'google', 'yandex', 'cloudflare'" \  
&& DST="'cloudflare', 'de.dnsmaschine.net', 'd0wn-nl-ns4', 'dnscrypt.eu-nl',
'doh-crypto-sx', 'dnscrypt.nl-ns0', 'dnscrypt.eu-dk', 'scaleway-fr',
'ipredator', 'flatty.co'" \  
&& sed -i "s/$SRC/$DST/" dnscrypt-proxy.toml \  
&& SRC="\\['127.0.0.1:53', '\\[::1\\]:53'\\]" \  
&& DST="['0.0.0.0:53']" \  
&& sed -i "s/$SRC/$DST/" dnscrypt-proxy.toml \  
&& sed -i "s/require_dnssec = false/require_dnssec = true/" dnscrypt-
proxy.toml \  
&& sed -i "s/daemonize = false/daemonize = true/" dnscrypt-proxy.toml \  
&& sed -i "s/9.9.9.9/${FALLBACK_RESOLVER}/g" dnscrypt-proxy.toml \  
&& mv example-blacklist.txt blacklist.txt \  
&& sed -i -E "s/# blacklist_file = 'blacklist.txt'/blacklist_file =
'blacklist.txt'/" dnscrypt-proxy.toml \  
&& mv example-whitelist.txt whitelist.txt \  
&& sed -i -E "s/# whitelist_file = 'whitelist.txt'/whitelist_file =
'whitelist.txt'/" dnscrypt-proxy.toml \  
&& mv example-cloaking-rules.txt cloaking-rules.txt \  
&& sed -i -E "s/# cloaking_rules = 'cloaking-rules.txt'/cloaking_rules =
'cloaking-rules.txt'/" dnscrypt-proxy.toml \  
&& mv example-forwarding-rules.txt forwarding-rules.txt \  
&& sed -i -E "s/# forwarding_rules = 'forwarding-rules.txt'/forwarding_rules =
'forwarding-rules.txt'/" dnscrypt-proxy.toml \  
&& printf "nameserver 127.0.0.1\noptions edns0 single-request-reopen" >
/etc/resolv.conf  
  
HEALTHCHECK CMD dig @127.0.0.1 reddit.com || exit 1  
  
EXPOSE 53:53/tcp 53:53/udp  
CMD ["/opt/dnscrypt-proxy/dnscrypt-proxy"]  

