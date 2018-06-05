# Prosody in Debian  
# Version 0.1  
FROM debian:jessie  
MAINTAINER Hong Xu <hong@topbug.net>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y prosody  
RUN apt-get install -y --no-install-recommends \  
ca-certificates \  
lua-dbi-mysql \  
lua-dbi-postgresql \  
lua-dbi-sqlite3 \  
lua-ldap \  
lua-zlib \  
mercurial  
  
RUN mkdir -vp /var/run/prosody && chown -vR prosody.prosody /var/run/prosody  
  
RUN ln -sv /dev/stdout /var/log/prosody/prosody.log && \  
ln -sv /dev/stderr /var/log/prosody/prosody.err && \  
chown -vR prosody.prosody /var/log/prosody  
  
# install additional modules  
RUN hg clone https://hg.prosody.im/prosody-modules/
/usr/lib/prosody/additional_modules  
  
# modify a few settings: do not run as daemon; add the additional modules into  
# the plugin path; log to console not to any file.  
RUN sed -ri \  
-e 's/daemonize = true/daemonize = false/' \  
-e '1s/^/prosody_user = "prosody"\nplugin_paths = \\{ "\/usr\/lib\/prosody\/additional_modules" \\}/' \  
-e 's/\/var\/log\/prosody\/prosody.log/\\*console/' \  
-e 's/\/var\/log\/prosody\/prosody.err/\\*console/' \  
/etc/prosody/prosody.cfg.lua  
  
EXPOSE 5222 5223 5269 5298  
ADD run.sh /usr/local/bin/run.sh  
  
CMD ["/usr/local/bin/run.sh"]  

