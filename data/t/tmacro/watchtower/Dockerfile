FROM tmacro/python:latest  
  
ENV DOCKERGEN_VER 0.7.3  
  
ADD https://github.com/jwilder/docker-
gen/releases/download/${DOCKERGEN_VER}/docker-gen-linux-
amd64-${DOCKERGEN_VER}.tar.gz /tmp  
  
ADD ./scripts/reload-haproxy ./scripts/install-certificates /usr/bin/  
  
RUN apk_add haproxy git openssl-dev gcc python3-dev linux-headers musl-dev
libffi-dev \  
&& tar -C /usr/bin -xvzf /tmp/docker-gen-linux-amd64-${DOCKERGEN_VER}.tar.gz \  
&& git clone https://github.com/certbot/certbot.git /tmp/certbot \  
&& cd /tmp/certbot \  
&& python setup.py install \  
&& cd certbot-dns-cloudflare \  
&& python setup.py install \  
&& cd /tmp \  
&& rm -rf /tmp/* \  
&& mkdir -p /etc/haproxy/certs.d \  
&& mkdir -p /etc/letsencrypt/renewal-hooks/post \  
&& ln -s /usr/bin/install-certificates /etc/letsencrypt/renewal-
hooks/post/00-install-certificates \  
&& ln -s /usr/bin/reload-haproxy /etc/letsencrypt/renewal-
hooks/post/10-reload-haproxy  
  
ADD ./s6 /etc  
ADD ./templates/haproxy.cfg.tmpl /etc/haproxy/haproxy.cfg.tmpl  
ADD ./scripts/503.http /etc/haproxy/503.http

