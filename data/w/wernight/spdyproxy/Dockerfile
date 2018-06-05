FROM node:0.10-slim  
  
RUN set -x \  
# Install SPDY Proxy.  
&& npm install -g spdyproxy \  
# Add a non-root user.  
&& useradd --system --uid 1593 \--shell /usr/sbin/nologin -M spdy \  
# Create a directory to hold TLS keys.  
&& mkdir /ssl \  
&& chown -R spdy:spdy /ssl \  
# Install dumb-init  
# https://github.com/Yelp/dumb-init  
&& DUMP_INIT_URI=$(curl -L https://github.com/Yelp/dumb-init/releases/latest |
grep -Po '(?<=href=")[^"]+_amd64(?=")') \  
&& curl -Lo /usr/local/bin/dumb-init "https://github.com/$DUMP_INIT_URI" \  
&& chmod +x /usr/local/bin/dumb-init  
  
VOLUME /ssl  
  
EXPOSE 44300  
COPY entrypoint.sh /  
  
USER spdy  
  
ENTRYPOINT ["dumb-init", "/entrypoint.sh"]  

