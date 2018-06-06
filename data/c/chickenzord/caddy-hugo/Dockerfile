FROM abiosoft/caddy:0.10.12  
ENV HUGO_VERSION=0.39  
RUN wget -O /tmp/hugo.tar.gz
http://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.tar.gz
\  
&& tar -xzf /tmp/hugo.tar.gz -C /usr/bin hugo \  
&& rm -f /tmp/hugo.tar.gz  
  
COPY Caddyfile /etc/Caddyfile  

