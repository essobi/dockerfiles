FROM debian:jessie  
MAINTAINER Stefan Reuter <docker@reucon.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install prosody  
COPY prosody-debian-packages.key /  
RUN set -x \  
&& apt-key add /prosody-debian-packages.key \  
&& echo "deb http://packages.prosody.im/debian jessie main" \  
> /etc/apt/sources.list.d/prosody.list \  
&& apt-get update -qq \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
lua-bitop \  
lua-cyrussasl \  
lua-dbi-mysql \  
lua-dbi-postgresql \  
lua-dbi-sqlite3 \  
lua-event \  
lua-ldap \  
lua-sec \  
lua-zlib \  
mercurial \  
prosody-0.10 \  
&& hg clone https://hg.prosody.im/prosody-modules
/usr/lib/prosody/additional_modules \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure prosody  
RUN set -x \  
&& sed -ri \  
-e '/Virtual hosts/,$d' \  
-e '/log = \\{/,/\\}/s/^/-- /' \  
-e '/ssl = \\{/,/\\}/s/^/-- /' \  
/etc/prosody/prosody.cfg.lua \  
&& echo 'daemonize = false' >>/etc/prosody/prosody.cfg.lua \  
&& echo 'log = "*console"' >>/etc/prosody/prosody.cfg.lua \  
&& echo 'plugin_paths = {\n "/usr/lib/prosody/additional_modules";\n}' >>
/etc/prosody/prosody.cfg.lua \  
&& echo 'Include "/etc/prosody/conf.d/*.lua"' >> /etc/prosody/prosody.cfg.lua  
  
VOLUME [ "/etc/prosody/conf.d", "/etc/prosody/certs", "/var/lib/prosody" ]  
  
# Expose proxy65 port  
EXPOSE 5000  
# Expose c2s port  
EXPOSE 5222  
# Expose s2s port  
EXPOSE 5269  
# Expose http port  
EXPOSE 5280  
# Expose https port  
EXPOSE 5281  
USER prosody  
  
ENV __FLUSH_LOG 1  
CMD [ "/usr/bin/lua5.1", "/usr/bin/prosody" ]  

