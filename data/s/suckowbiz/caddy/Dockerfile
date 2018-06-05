FROM suckowbiz/base  
  
LABEL maintainer="Tobias Suckow <tobias@suckow.biz>"  
  
ENV CADDY_VERSION=v0.10.14  
ENV CADDY_DOWNLOAD_ROOT=https://github.com/mholt/caddy/releases/download \  
CADDY_REMOTE_NAME="caddy_${CADDY_VERSION}_linux_amd64" \  
# if set, Caddy will use this folder to store assets instead of the default
$HOME/.caddy.  
CADDYPATH=/var/lib/caddy/.caddy \  
PATH="${PATH}:/var/lib/caddy"  
ENV CADDY_TARBALL=${CADDY_REMOTE_NAME}.tar.gz  
  
RUN apt-get install --quiet --quiet --yes --no-install-recommends \  
libcap2-bin  
RUN mkdir --parent "${CADDYPATH}"  
  
WORKDIR /var/lib/caddy  
RUN curl \  
\--fail \  
\--location \  
\--remote-name \  
\--show-error \  
"${CADDY_DOWNLOAD_ROOT}/${CADDY_VERSION}/${CADDY_TARBALL}" \  
&& tar --extract --file "${CADDY_TARBALL}" \  
&& rm --force "${CADDY_TARBALL}" \  
&& ls -la \  
# allow caddy to bind to :80 and :443  
&& setcap CAP_NET_BIND_SERVICE=+eip caddy  
  
VOLUME "${CADDYPATH}"  
  
ENTRYPOINT ["/entrypoint.sh", "caddy"]  
CMD ["-agree", "-log", "stdout" ]  

